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
        elif evento.type == pygame.KEYDOWN:
            if evento.key == K_LEFT:
                posX -= velocidad
            elif evento.key == K_RIGHT:
                posX += velocidad
        elif evento.type == pygame.KEYUP:
            if evento.key == K_LEFT:
                print("tecla izquierda liberada")
            elif evento.key == K_RIGHT:
                print("tecla derecha liberada")

    posX = pygame.mouse.get_pos()[0]-25 #recogemos la coordenada en X del cursor para la posicion X de nuestra imagen, se corrige 25 pixels para centrar la imagen al puntero
    posY = pygame.mouse.get_pos()[1]-25 #recogemos la coordenada en Y del cursor para la posicion X de nuestra imagen, se corrige 25 pixels para centrar la imagen al puntero

    pygame.display.update()
