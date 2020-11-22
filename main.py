import sys, os
import pygame as pg
import Libreria.tilerender as tilerd
import Libreria.constantes as cnt




if __name__ == "__main__":
	pg.init()
	pantalla = pg.display.set_mode((cnt.ANCHO, cnt.ALTO))
	main_rect = pantalla.get_rect()


	"""Cargar el archivo tmx del directorio señalado,
	crea el objeto tilerender y carga el archivo .tmx."""
	tmx_file = "Sprites/archivosmapa/tiledmapa.tmx"
	tile_renderer = tilerd.Renderer(tmx_file)


	"""Crea el mapa usando el metodo make_map().
	  Para ser usado en la pantalla."""
	map_surface = tile_renderer.make_map()
	map_rect = map_surface.get_rect()

	fps_clock = pg.time.Clock()
	while(True):
		pantalla.blit(map_surface, map_rect)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

		pg.display.update()
		fps_clock.tick(60)



 