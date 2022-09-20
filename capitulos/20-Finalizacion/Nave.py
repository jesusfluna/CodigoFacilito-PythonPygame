import pygame
import Proyectil


class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load("../imagenes/nave.jpg")
        self.imagen_explosion = pygame.image.load("../imagenes/explosion.jpg")

        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto - 30

        self.lista_disparo = []
        self.vida = True
        self.velocidad = 20
        self.sonido_disparo = pygame.mixer.Sound("../sonidos/disparo.wav")
        self.sonido_destruccion = pygame.mixer.Sound("../sonidos/dead.wav")

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
            elif self.rect.right > 870:
                self.rect.right = 640

    def disparar(self, x, y):
        mi_proyectil = Proyectil.Proyectil(x, y, "../imagenes/disparoa.jpg", True)
        self.lista_disparo.append(mi_proyectil)
        self.sonido_disparo.play()

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)

    def destruccion(self):
        self.sonido_destruccion.play()
        self.vida = False
        self.velocidad = 0
        self.ImagenNave = self.imagen_explosion
