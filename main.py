import sys, os
import pygame as pg
import Libreria.tilerender as tilerd
import Libreria.constantes as cnt
import Libreria.personajes as pj

def movercolliders(collis, trigg, iX, iY):
	for i in collis:
		i[0] = i[0] + iX # Cambio en X
		i[1] = i[1] + iY # Cambio en Y

	for i in trigg:
		i[0] = i[0] + iX 
		i[1] = i[1] + iY  

def inicializarcolliders(collis, trigg, iY):
	for i in collis:
		i[1] += iY

	for i in trigg:
		i[1] += iY


def moverposenemigos(pos, iX, iY):
	pos[0] += iX	#posicion en X
	pos[1] += iY	#posicion en Y

	if(enemigosA):
		for enemy in enemigosA:
			enemy.rect.x += iX
			enemy.rect.y += iY

	return pos




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


	"""Creacion de los colliders. almacenados en "blockers"."""
	blockers = []
	triggers = []
	tilewidth = tile_renderer.tmx_data.tilewidth
	for tile_object in tile_renderer.tmx_data.objects:
	    properties = tile_object.__dict__
	    #print(properties)
	    #print(properties['x'], properties['x'])
	    if(properties['type'] == 'choza'):
	    	x = properties['x']
	    	y = properties['y']
	    	width = properties['width']
	    	height = properties['height']
	    	new_rect = pg.Rect(x, y, width, height)
	    	triggers.append(new_rect)
	    else:
	    	x = properties['x']
	    	y = properties['y']
	    	width = properties['width']
	    	height = properties['height']
	    	new_rect = pg.Rect(x, y, width, height)
	    	blockers.append(new_rect)



	"""Creacion del personaje y el grupo de personajes """
	#crear grupo
	jugadores = pg.sprite.Group()
	enemigosA = pg.sprite.Group()  

	#objeto jugador
	j = pj.Jugador(blockers, triggers, enemigosA)
	jugadores.add(j)

	
	#Posicion y velocidad de la "camara o pantalla" 
	f_x = 0
	f_velx = 0
	f_y = cnt.ALTO- alto_fondo
	f_vely = 0

	#Posicion enemigos choza1
	pec1 = [576, 194]

	pec1 = moverposenemigos(pec1, 0, cnt.ALTO- alto_fondo)
	inicializarcolliders(j.blockers, j.triggers, cnt.ALTO- alto_fondo)

	#print(j.blockers[0])
	#j.blockers[0][1] = j.blockers[0][1] + 30 
	#print(j.blockers[0])

	# Interfaz
	fuente=pg.font.Font(None,32)

	fps_clock = pg.time.Clock()
	while(True):
		keys = pg.key.get_pressed()
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

		
		# Control mapa y colisiones
		if(j.rect.x > (cnt.ANCHO-150) and f_x > (cnt.ANCHO-ancho_fondo) 
			and f_velx < 0):
			f_x += f_velx
			movercolliders(j.blockers, j.triggers, f_velx, 0)
			moverposenemigos(pec1, f_velx, 0)
			j.velx = 0 

		if(j.rect.x < 150 and f_x < 0 and f_velx > 0):
			f_x += f_velx
			movercolliders(j.blockers, j.triggers, f_velx, 0)
			moverposenemigos(pec1, f_velx, 0)
			j.velx = 0 

		if(j.rect.y > (cnt.ALTO-150) and f_y > (cnt.ALTO-alto_fondo)
			and f_vely < 0):
			f_y += f_vely
			movercolliders(j.blockers, j.triggers, 0, f_vely)
			moverposenemigos(pec1, 0, f_vely) 
			j.vely = 0 

		if(j.rect.y < 150 and f_y < 0 and f_vely > 0):
			f_y += f_vely
			movercolliders(j.blockers, j.triggers, 0, f_vely)
			moverposenemigos(pec1, 0, f_vely) 
			j.vely = 0      


		#Control enemigo
		if(j.zone and (not enemigosA)):
			#objeto enemigo A
			print("Creado")
			e = pj.EnemigoA(blockers, triggers, pec1, j)
			enemigosA.add(e)
			j.zone = False



		#HUD
		info_salud='Salud: ' + str(j.salud)
		texto=fuente.render(info_salud,True, cnt.BLANCO)
			
		# Actualizar pantalla
		pantalla.blit(map_surface, [f_x,f_y])

		enemigosA.update()
		enemigosA.draw(pantalla)

		jugadores.update(keys)
		jugadores.draw(pantalla)
		

		pantalla.blit(texto,[50,30])

		pg.display.update()
		fps_clock.tick(60)



 