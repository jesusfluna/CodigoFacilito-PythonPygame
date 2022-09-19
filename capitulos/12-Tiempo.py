import pygame
import sys
from random import randint
from pygame import *
import time

pygame.init()
ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola PyGame")

fuente = pygame.font.SysFont("Arial", 30)

aux = 1 #variable auxiliar para controlar los segundos
while True:
    time.sleep(0.01)
    ventana.fill((255, 255, 255))
    Tiempo = pygame.time.get_ticks()/1000#Entero con el valor en milisegundos desde que pygame.init() se ejecutó, en segundos con el /1000

    if aux == Tiempo: #Asi solo se muestra el mensage del print en cada segundo redondo
        aux += 1
        print(Tiempo)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    contador = fuente.render("Tiempo : "+str(Tiempo), 0, (120, 70, 0))
    ventana.blit(contador, (100, 100))
    pygame.display.update()
