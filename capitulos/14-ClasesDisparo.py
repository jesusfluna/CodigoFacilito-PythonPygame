import pygame
import sys
from random import randint
from pygame import *
from pygame.locals import *
import time

# variables globales
ancho, alto = 900, 400


class nave_espacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load("imagenes/nave.jpg")

        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto - 30

        self.listaDisparo = []
        self.vida = True
        self.velocidad = 20

    def movimiento(self):
        if self.vida:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > ancho - 30:
                self.rect.right = ancho - 60

    def disparar(self, x, y):
        mi_proyectil = Proyectil(x, y)
        self.listaDisparo.append(mi_proyectil)

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image_proyectil = pygame.image.load("imagenes/disparoa.jpg")
        self.rect = self.image_proyectil.get_rect()
        self.velocidad_disparo = 5
        self.rect.top = pos_y
        self.rect.left = pos_x

    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidad_disparo

    def dibujar(self, superficie):
        superficie.blit(self.image_proyectil, self.rect)


def space_invader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Hola PyGame")
    imagen_fondo = pygame.image.load("imagenes/Fondo.jpg")

    jugador = nave_espacial()

    demo_proyectil = Proyectil(ancho/2, alto-30)
    en_juego = True
    while True:
        time.sleep(0.01)

        jugador.movimiento()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if en_juego:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.rect.left -= jugador.velocidad
                    elif evento.key == K_RIGHT:
                        jugador.rect.right += jugador.velocidad
                    elif evento.key == K_SPACE:
                        x, y = jugador.rect.center
                        jugador.disparar(x, y)

        ventana.blit(imagen_fondo, (0, 0))

        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top < 10:
                    jugador.listaDisparo.remove(x)

        jugador.dibujar(ventana)
        pygame.display.update()


space_invader()
