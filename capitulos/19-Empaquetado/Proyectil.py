import pygame


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
