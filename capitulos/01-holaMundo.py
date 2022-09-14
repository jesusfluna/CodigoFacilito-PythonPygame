"""01-Ventana Hola Mundo"""
import pygame, sys
from pygame import *

pygame.init() #Obligatorio hacerlo al inicio, es necesario para la inicializacion del modulo pygame y hacer uso de sus funciones

ventana = pygame.display.set_mode((400, 300))#creacion de una ventana con los valores de ancho y largo
pygame.display.set_caption("Hola mundo")#Colocamos un titulo en la ventana

while True: #mostramos la ventana, para mantenerla a la vista hacemos uso de un bucle infinito
    for evento in pygame.event.get():#recorremos la lista de eventos de pygame para comprobar el que nos interese
        if evento.type == QUIT:#comporbamos si hay un evento QUIT
            pygame.quit()   #Cerramos el modulo de pygame
            sys.exit()  #Cerramos la aplicacion

    pygame.display.update() #actualizamos la venana constantemente