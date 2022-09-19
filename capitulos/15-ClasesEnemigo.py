import pygame
import sys
from random import randint
from pygame import *
from pygame.locals import *
import time

# variables globales
ancho, alto = 900, 480


class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load("imagenes/nave.jpg")

        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto - 30

        self.listaDisparo = []
        self.vida = True
        self.velocidad = 20

    def movimiento_derecha(self):
        self.rect.right += self.velocidad
        self.__movimiento()

    def movimiento_izquierda(self):
        self.rect.left -= self.velocidad
        self.__movimiento()

    def __movimiento(self):
        if self.vida:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > ancho - 30:
                self.rect.right = ancho - 60

    def disparar(self, x, y):
        mi_proyectil = Proyectil(x, y, "imagenes/disparoa.jpg", True)
        self.listaDisparo.append(mi_proyectil)

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)

        self.image_proyectil = pygame.image.load(ruta)
        self.rect = self.image_proyectil.get_rect()
        self.velocidad_disparo = 5
        self.rect.top = pos_y
        self.rect.left = pos_x

        self.disparo_personaje = personaje

    def trayectoria(self):
        if self.disparo_personaje:
            self.rect.top = self.rect.top - self.velocidad_disparo
        else:
            self.rect.top = self.rect.top + self.velocidad_disparo



    def dibujar(self, superficie):
        superficie.blit(self.image_proyectil, self.rect)


class Invasor(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.imagenA = pygame.image.load("imagenes/marcianoA.jpg")
        self.imagenB = pygame.image.load("imagenes/MarcianoB.jpg")

        self.lista_imagenes = (self.imagenA, self.imagenB)
        self.pos_imagen = 0
        self.imagen_invasor = self.lista_imagenes[self.pos_imagen]

        self.rect = self.imagen_invasor.get_rect()
        self.velocidad = 5
        self.lista_disparo = []
        self.rect.top = pos_y
        self.rect.left = pos_x

        self.rango_disparo = 5
        self.tiempo_cambio = 1

        self.derecha = True
        self.contador = 0
        self.max_descenso = self.rect.top + 40

    def comportamiento(self, tiempo):
        self.__movimientos()
        self.__ataque()
        self.pos_imagen = int(tiempo % 2)

    def dibujar(self, superficie):
        self.imagen_invasor = self.lista_imagenes[self.pos_imagen]
        superficie.blit(self.imagen_invasor, self.rect)

    def __ataque(self):
        if randint(0, 100) < self.rango_disparo:
            self.__disparo()

    def __disparo(self):
        x, y = self.rect.center
        mi_proyectil = Proyectil(x, y, "imagenes/disparob.jpg", False)
        self.lista_disparo.append(mi_proyectil)

    def __movimientos(self):
        if self.contador < 3:
            self.__movimiento_lateral()
        else:
            self.__movimiento_descenso()

    def __movimiento_lateral(self):
        if self.derecha:
            self.rect.left = self.rect.left + self.velocidad
            if self.rect.left > 700:
                self.derecha = False
                self.contador += 1
        else:
            self.rect.left = self.rect.left - self.velocidad
            if self.rect.left < 0:
                self.derecha = True

    def __movimiento_descenso(self):
        if self.max_descenso == self.rect.top:
            self.contador = 0
            self.max_descenso = self.rect.top + 40
        else:
            self.rect.top += 1


def space_invader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Hola PyGame")
    imagen_fondo = pygame.image.load("imagenes/Fondo.jpg")

    jugador = NaveEspacial()
    enemigo = Invasor(100, 100)

    reloj = pygame.time.Clock()
    en_juego = True
    while True:
        #time.sleep(0.01)
        reloj.tick(60)# "Frames" por segundo
        tiempo = pygame.time.get_ticks()/1000

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if en_juego:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.movimiento_izquierda()
                    elif evento.key == K_RIGHT:
                        jugador.movimiento_derecha()
                    elif evento.key == K_SPACE:
                        x, y = jugador.rect.center
                        jugador.disparar(x, y)

        ventana.blit(imagen_fondo, (0, 0))

        enemigo.comportamiento(tiempo)
        enemigo.dibujar(ventana)
        jugador.dibujar(ventana)
        if len(jugador.listaDisparo) > 0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top < 10:
                    jugador.listaDisparo.remove(x)

        if len(enemigo.lista_disparo) > 0:
            for x in enemigo.lista_disparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top > 900:
                    enemigo.lista_disparo.remove(x)

        pygame.display.update()


space_invader()
