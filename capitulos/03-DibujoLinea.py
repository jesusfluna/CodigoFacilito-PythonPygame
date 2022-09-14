import pygame
import sys
from pygame import *

pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola PyGame")

color = pygame.Color(70, 80, 150)
pygame.draw.line(ventana, color, (60, 80), (160, 100), 3)#Recurso pygame para pintar una linea, {donde, color, puntoInicio(x,y), puntoDestino(x,y), grosor}

print(color.r) #nivel de saturacion del color en R
print(color.g) #nivel de saturacion del color en G
print(color.b) #nivel de saturacion del color en B

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
