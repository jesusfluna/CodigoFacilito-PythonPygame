import pygame
import sys
from pygame import *

pygame.init()

ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola PyGame")

pygame.draw.rect(ventana, pygame.Color(130, 70, 70), (0, 0, 100, 50))#Dibujo de un rectangulo, {donde, color, (coordenadas xy de esquina superior izuierda, ancho, alto)}
pygame.draw.polygon(ventana, pygame.Color(90, 180, 70), ((140, 0), (291, 106), (237, 277), (56, 277), (0, 106))) #Dibujo de un poligono, {donde,color, tupla de puntos que forman el poligono}
pygame.draw.circle(ventana, pygame.Color(8, 70, 120), (80, 90), 20) #Dibujo de un circulo, {donde,color, coordenadaCentro, radio}

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
