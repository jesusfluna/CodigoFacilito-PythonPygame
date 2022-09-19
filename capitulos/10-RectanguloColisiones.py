import pygame
import sys
from random import randint
from pygame import *
import time

pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola PyGame")
posX, posY = 200, 100

velocidad = 2
derecha = True
rectangulo = pygame.Rect(0, 0, 100, 50)#Creamos un objeto de tipo rectangulo. {x, y, width, height}
rectangulo_dos = pygame.Rect(200, 200, 100, 50)#Creamos un objeto de tipo rectangulo. {x, y, width, height}

while True:
    time.sleep(0.01)
    ventana.fill(pygame.Color(255, 255, 255))
    pygame.draw.rect(ventana, (180, 70, 70), rectangulo_dos)  # Pintamos el rectangulo dos en nuestra ventana

    pygame.draw.rect(ventana, (180, 70, 70), rectangulo)#Pintamos el rectangulo en nuestra ventana
    rectangulo.left, rectangulo.top = pygame.mouse.get_pos()#posicionamos el rectangulo en la posicion del puntero del raton

    if rectangulo.colliderect(rectangulo_dos):
        velocidad = 0
        print("Colision detectada")

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    if derecha:
        if posX < 400 :
            posX += velocidad
            rectangulo_dos.left = posX #Movmiento del rectangulo dos
        else:
            derecha = False
    else:
        if posX > 1:
            posX -= velocidad
            rectangulo_dos.right = posX #movimiento del retanguo dos
        else:
            derecha = True
    pygame.display.update()
