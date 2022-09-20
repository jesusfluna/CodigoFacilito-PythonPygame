import pygame
import sys
from pygame.locals import *
from Nave import NaveEspacial
from Invasor import Invasor as Enemigo

# variables globales
ancho, alto = 900, 480
lista_enemigo = []


def cargar_enemigos():
    pos_x = 100
    for x in range(1, 5):
        enemigo = Enemigo(pos_x, 100, 40, '../imagenes/marcianoA.jpg', '../imagenes/MarcianoB.jpg')
        lista_enemigo.append(enemigo)
        pos_x += 200

    pos_x = 100
    for x in range(1, 5):
        enemigo = Enemigo(pos_x, 0, 40, '../imagenes/Marciano2A.jpg', '../imagenes/Marciano2B.jpg')
        lista_enemigo.append(enemigo)
        pos_x += 200

    pos_x = 100
    for x in range(1, 5):
        enemigo = Enemigo(pos_x, -100, 40, '../imagenes/marciano3A.jpg', '../imagenes/Marciano3B.jpg')
        lista_enemigo.append(enemigo)
        pos_x += 200


def space_invader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Hola PyGame")
    imagen_fondo = pygame.image.load("../imagenes/Fondo.jpg")

    pygame.mixer.music.load("../sonidos/bso.mp3")
    pygame.mixer.music.play(3)

    jugador = NaveEspacial(ancho, alto)
    cargar_enemigos()

    reloj = pygame.time.Clock()
    en_juego = True
    while True:
        reloj.tick(60)
        tiempo = pygame.time.get_ticks()/1000

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if en_juego:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.movimiento_izquierda()
                    elif evento.key == K_RIGHT:
                        jugador.movimiento_derecha()
                    elif evento.key == K_SPACE:
                        x, y = jugador.rect.center
                        jugador.disparar(x, y)

        ventana.blit(imagen_fondo, (0, 0))

        jugador.dibujar(ventana)
        if len(jugador.lista_disparo) > 0:
            for x in jugador.lista_disparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top < 10:
                    jugador.lista_disparo.remove(x)
                else:
                    for enemigo in lista_enemigo:
                        if x.rect.colliderect(enemigo.rect):
                            lista_enemigo.remove(enemigo)
                            jugador.lista_disparo.remove(x)

        if len(lista_enemigo) > 0:
            for enemigo in lista_enemigo:
                enemigo.comportamiento(tiempo)
                enemigo.dibujar(ventana)

                if enemigo.rect.colliderect(jugador.rect):
                    pass

                if len(enemigo.lista_disparo) > 0:
                    for x in enemigo.lista_disparo:
                        x.dibujar(ventana)
                        x.trayectoria()

                        if x.rect.colliderect(jugador.rect):
                            pass

                        if x.rect.top > 900:
                            enemigo.lista_disparo.remove(x)
                        else:
                            for disparo in jugador.lista_disparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.lista_disparo.remove(disparo)
                                    enemigo.lista_disparo.remove(x)

        pygame.display.update()


space_invader()
