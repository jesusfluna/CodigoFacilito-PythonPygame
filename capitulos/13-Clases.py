import pygame
import sys
from random import randint
from pygame import *
from pygame.locals import *
import time

# variables globales
ancho, alto = 900, 400

class naveEspacial(pygame.sprite.Sprite):
    """Clase para las naves que hereda de pygame sprite"""
    def __init__(self): # valores iniciales al instanciar el objeto de la clase
        pygame.sprite.Sprite.__init__(self) # Instanciacion del objeto self
        self.ImagenNave = pygame.image.load("imagenes/nave.jpg") # carga de la imagen

        self.rect = self.ImagenNave.get_rect() # Devuleve un rectangulo de la nave
        self.rect.centerx = ancho/2 # posicionamos la nave a la mitad de la pantalla en X
        self.rect.centery = alto - 30 # posicionamos la nave casi abajo del todo en Y

        self.listaDisparo = [] # Lista de disparos
        self.vida = True # Vida de la nave
        self.velocidad = 20

    def movimiento(self): #Logica de movimiento, parecido a capitulos anteriores
        if self.vida:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > ancho - 30:
                self.rect.right = ancho - 60

    def dispara(self):
        print("Disparo")

    def dibujar(self, superficie): # Funcion para autodibujarse en una superficie
            superficie.blit(self.ImagenNave, self.rect)


# Encapsulamos el lanzamiento de la aplicación en una función
def spaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Hola PyGame")
    ImagenFondo = pygame.image.load("imagenes/Fondo.jpg") # Cargamos una imagen de fondo

    jugador = naveEspacial() # Creamos un objeto naveEspacial en nuestra aplicación
    enJuego = True
    while True:
        time.sleep(0.01)

        jugador.movimiento()#llamamos constantemente al metodo de movimiento

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if enJuego:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.rect.left -= jugador.velocidad
                    elif evento.key == K_RIGHT:
                        jugador.rect.right += jugador.velocidad
                    elif evento.key == K_SPACE:
                        jugador.dispara()

        ventana.blit(ImagenFondo, (0, 0)) # Ponemos nuestro fondo en la ventana
        jugador.dibujar(ventana) # Dibujamos la nave
        pygame.display.update()


spaceInvader() #Ejemcutamos el metodo de lanzamiento de la aplicacion
