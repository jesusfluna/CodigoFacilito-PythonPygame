import pygame
import sys
from pygame import *

pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola PyGame")

mi_imagen = pygame.image.load("imagenes/ovni.png")#Carga de la imagen de la ruta
posX, posY = 130, 70

ventana.blit(mi_imagen, (posX, posY))#Pintamos la imagen en la ventana en la posicion XY

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
