import pygame, sys
from pygame import *

Color = (0, 140, 60) #Creacion de un color directamente como un array de python con valores RGB
ColorDos = pygame.Color(255, 120, 9) #Proceso analogo pero usando el modulo especifico de pygame para la creacion del array RGB
pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola mundo")

while True:
    ventana.fill(ColorDos) #Rellenamos la ventana con uno de los colores definidos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()