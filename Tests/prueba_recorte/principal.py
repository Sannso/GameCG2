import pygame
import random
import recortar
import os

ANCHO=1200
ALTO=800

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    Rutabase = '../'
    Rutarel = '../Test_personaje/character.png'
    Rutasol = os.path.join(Rutabase, Rutarel)
    
    imagen = os.path.abspath(Rutasol)

    list_cuadritos = []
    list_cuadritos = recortar.Recortar(list_cuadritos, imagen, 18, 8)


    pantalla.blit(list_cuadritos[0][0],[100,100])
    pantalla.blit(list_cuadritos[0][1],[200,100])

    pygame.display.flip()
    fin=False
    while not fin :
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
