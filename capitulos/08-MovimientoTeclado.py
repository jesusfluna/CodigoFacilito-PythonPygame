import pygame
import sys
from random import randint
from pygame import *
import time

pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola PyGame")

mi_imagen = pygame.image.load("imagenes/ovni.png")
posX, posY = randint(10, 350), randint(10, 250)

velocidad = 5

while True:
    time.sleep(0.01)
    ventana.fill(pygame.Color(255, 255, 255))
    ventana.blit(mi_imagen, (posX, posY))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN: #Añadimos el evento en caso de presionar la tecla
            if evento.key == K_LEFT:#si es la izquierda movemos la imagen a la izquieda
                posX -= velocidad
            elif evento.key == K_RIGHT:#Si es la derecha movemos la imagen a la derecha
                posX += velocidad
        elif evento.type == pygame.KEYUP: #Analogamente al punto anterior comprobamos cuando se liberan las teclas y pintamos un mensaje
            if evento.key == K_LEFT:
                print("tecla izquierda liberada")
            elif evento.key == K_RIGHT:
                print("tecla derecha liberada")
    pygame.display.update()
