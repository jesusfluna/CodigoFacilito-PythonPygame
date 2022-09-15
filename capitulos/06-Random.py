import pygame
import sys
from random import randint
from pygame import *

pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola PyGame")

mi_imagen = pygame.image.load("imagenes/ovni.png")
posX, posY = randint(10, 350), randint(10, 250) #Generamos las posiciones X e Y para nuestra imagen de manera aleatoria

ventana.blit(mi_imagen, (posX, posY))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
