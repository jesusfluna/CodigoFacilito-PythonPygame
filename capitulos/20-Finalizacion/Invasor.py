import pygame
from random import randint
import Proyectil


class Invasor(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, distancia, imagen_uno, imagen_dos):
        pygame.sprite.Sprite.__init__(self)

        self.imagenA = pygame.image.load(imagen_uno)
        self.imagenB = pygame.image.load(imagen_dos)

        self.lista_imagenes = (self.imagenA, self.imagenB)
        self.pos_imagen = 0
        self.imagen_invasor = self.lista_imagenes[self.pos_imagen]

        self.rect = self.imagen_invasor.get_rect()
        self.velocidad = 5
        self.lista_disparo = []
        self.rect.top = pos_y
        self.rect.left = pos_x

        self.rango_disparo = 2
        self.tiempo_cambio = 1

        self.derecha = True
        self.contador = 0
        self.max_descenso = self.rect.top + 40

        self.limite_derecha = pos_x + distancia
        self.limite_izquierda = pos_x - distancia

        self.conquista = False

    def comportamiento(self, tiempo):
        if not self.conquista:
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
        mi_proyectil = Proyectil.Proyectil(x, y, "../imagenes/disparob.jpg", False)
        self.lista_disparo.append(mi_proyectil)

    def __movimientos(self):
        if self.contador < 3:
            self.__movimiento_lateral()
        else:
            self.__movimiento_descenso()

    def __movimiento_lateral(self):
        if self.derecha:
            self.rect.left = self.rect.left + self.velocidad
            if self.rect.left > self.limite_derecha:
                self.derecha = False
                self.contador += 1
        else:
            self.rect.left = self.rect.left - self.velocidad
            if self.rect.left < self.limite_izquierda:
                self.derecha = True

    def __movimiento_descenso(self):
        if self.max_descenso == self.rect.top:
            self.contador = 0
            self.max_descenso = self.rect.top + 40
        else:
            self.rect.top += 1
