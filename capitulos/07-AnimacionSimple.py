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

velocidad = 2 #Numero de pixeles que se desplazara nuestra imagne
derecha = True #Sentido del movimiento de nuestra imagen


while True:
    time.sleep(0.01)#ponemos un tiempo de 'pausa' para que los procesos del bucle no sean tan rapidos que no podamos verlos adecuadamente
    ventana.fill(pygame.Color(255, 255, 255))#Ponemos un fondo blanco, con esto ademas eliminamos el 'arrastre' de la imagen
    ventana.blit(mi_imagen, (posX, posY))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    if derecha:#Logica de movimiento jugando con la posicion X e Y y el sentido del movimiento
        if posX < 400 - 50:#Tamaño de la ventana menos el tamaño de la imagne
            posX += velocidad
        else:
            derecha = False
    else:
        if posX > 1:
            posX -= velocidad
        else:
            derecha = True
    pygame.display.update()
