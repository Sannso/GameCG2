import sys, os
import pygame as pg
import Libreria.tilerender as tilerd
import Libreria.constantes as cnt
import Libreria.personajes as pj




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
	ancho_fondo = map_surface.get_rect()[2]
	alto_fondo = map_surface.get_rect()[3]
	print(ancho_fondo, alto_fondo)


	"""Creacion del personaje y el grupo de personajes """
	#crear grupo
	jugadores = pg.sprite.Group() 

	#objeto jugador
	j = pj.Jugador()
	jugadores.add(j)

	#Posicion y velocidad de la "camara o pantalla" 
	f_x = 0
	f_velx = 0
	f_y = 0
	f_vely = 0

	fps_clock = pg.time.Clock()
	while(True):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_LEFT:
					j.velx = -5
					j.vely = 0
					f_velx = 5
					f_vely = 0

				if event.key == pg.K_RIGHT:
					j.velx = 5
					j.vely = 0
					f_velx = -5
					f_vely = 0

				if event.key == pg.K_DOWN:
					j.velx = 0
					j.vely = 5
					f_vely = -5
					f_velx = 0

				if event.key == pg.K_UP:
					j.velx = 0
					j.vely = -5
					f_vely = 5
					f_velx = 0

			if event.type == pg.KEYUP:
				if (((event.key == pg.K_LEFT) and (j.velx < 0))
                 or ((event.key == pg.K_RIGHT) and (j.velx > 0))):
					j.velx = 0

				if (((event.key == pg.K_DOWN) and (j.vely > 0))
                 or ((event.key == pg.K_UP) and (j.vely < 0))):
					j.vely = 0

				if (((event.key == pg.K_LEFT) and (f_velx > 0))
                 or ((event.key == pg.K_RIGHT) and (f_velx < 0))):
					f_velx = 0

				if (((event.key == pg.K_DOWN) and (f_vely < 0))
                 or ((event.key == pg.K_UP) and (f_vely > 0))):
					f_vely = 0

		
		# Control
		if(j.rect.x > (cnt.ANCHO-150) and f_x > (cnt.ANCHO-ancho_fondo) 
			and f_velx < 0):
			f_x += f_velx
			j.velx = 0 

		if(j.rect.x < 150 and f_x < 0 and f_velx > 0):
			f_x += f_velx
			j.velx = 0 

		if(j.rect.y > (cnt.ALTO-150) and f_y > (cnt.ALTO-alto_fondo)
			and f_vely < 0):
			f_y += f_vely 
			j.vely = 0 

		if(j.rect.y < 150 and f_y < 0 and f_vely > 0):
			f_y += f_vely
			j.vely = 0      


		# Actualizar pantalla
		pantalla.blit(map_surface, [f_x,f_y])

		jugadores.update()
		jugadores.draw(pantalla)
		pg.display.update()
		fps_clock.tick(60)



 