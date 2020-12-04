import pygame
import configparser

animapersonaje = []

def recortar_imagen(nombre_imagen, ancho_imagen,alto_imagen,fila_):
    
    terreno = pygame.image.load(nombre_imagen)
    info = terreno.get_rect()
    ancho_pixeles = info[2]
    alto_pixeles = info[3]

    ancho_patron = ancho_pixeles/ancho_imagen
    alto_patron = alto_pixeles/alto_imagen

    #parametros  subsurface: posicion x, posicion y, ancho corte (ancho patron), alto corte(alto patron)

    for fila in range(alto_imagen):
        animapersonaje.append([])
        for col in range(ancho_imagen):
           cuadro = terreno.subsurface(ancho_patron*col, alto_patron*fila, ancho_patron, alto_patron)
           animapersonaje[fila_].append(cuadro)

