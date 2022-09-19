import pygame
import sys
from random import randint
from pygame import *
import time

pygame.init()
ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hola PyGame")

miFuente = pygame.font.Font(None, 30) #Creamos una fuente {fuente, tamaño}
miTexto = miFuente.render("Prueba fuente", 0, (200, 60, 80))#Creamos un texto con la fuente anterior {texto, antialis, color}

miFuenteSys = pygame.font.SysFont("Arial", 30)#Creamos una fuente con las del sistema {fuente, tamaño}
miTextoSys = miFuente.render("Prueba fuente sistema", 0, (200, 60, 80))#Creamos un texto con la fuente anterior {texto, antialis, color}

while True:

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    ventana.blit(miTexto, (0, 0)) #Dibujamos el texto en la ventana
    ventana.blit(miTextoSys, (100, 100)) #Dibujamos el texto en la ventana
    pygame.display.update()
