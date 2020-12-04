import sys, os
import pygame as pg
import random
import Libreria.tilerender as tilerd
import Libreria.constantes as cnt
import Libreria.personajes as pj
import Libreria.chocitas as ch
import Libreria.objetos as obj
import Libreria.animaciones as ani

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
	if(pos):
		pos[0] += iX	#posicion en X
		pos[1] += iY	#posicion en Y
	return pos

# Como su nombre lo indica mueve todos los enemigos para que parezcan estaticos si es  el caso
def movergrupoenemigos(iX, iY):
	if(enemigosA):
		for enemy in enemigosA:
			enemy.rect.x += iX
			enemy.rect.y += iY


def movergrupoobjetos(iX, iY):
	if(objetosG):
		for g in objetosG:
			g.rect.x += iX
			g.rect.y += iY

#Mueve las listas con posiciones
def moverlist_ene_cho(lista, iX, iY):
	for i in lista:
		i = moverposenemigos(i, iX, iY)
	return lista


# Imprime las chozas
def printchocitas(pantalla, img, lista):
	for i in lista:
		if(i):
			pantalla.blit(img, i)


def crearModificador(pos):
	deter = random.random()
	if(deter < 0.1):
		ob = obj.Modificador(imgpower, "power", pos, jugadores, objetosG)
		objetosG.add(ob)

	elif(deter < 0.6):
		ob = obj.Modificador(imgvelatk, "velatk", pos, jugadores, objetosG)
		objetosG.add(ob)

	elif(deter <= 1):
		ob = obj.Modificador(imgvida, "vida", pos, jugadores, objetosG)
		objetosG.add(ob)

	


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
	blockerpjs = []
	triggers = []
	tilewidth = tile_renderer.tmx_data.tilewidth
	for tile_object in tile_renderer.tmx_data.objects:
	    properties = tile_object.__dict__
	    #print(properties)
	    #print(properties['x'], properties['x'])
	    if(properties['type'] == 'choza' or properties['type'] == 'chocita'):
	    	x = properties['x']
	    	y = properties['y']
	    	width = properties['width']
	    	height = properties['height']
	    	new_rect = pg.Rect(x, y, width, height)
	    	triggers.append(new_rect)

	    elif(properties['type'] == 'chocolli'):
	    	x = properties['x']
	    	y = properties['y']
	    	width = properties['width']
	    	height = properties['height']
	    	new_rect = pg.Rect(x, y, width, height)
	    	blockerpjs.append(new_rect)
	    	blockers.append(new_rect)

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
	objetosG = pg.sprite.Group()

	#objeto jugador
	sgolpe = pg.mixer.Sound('Sprites/Sonido/TailWhip.flac')
	animaciones = ani.aniPrincipal()
	j = pj.Jugador(blockers, triggers, blockerpjs, enemigosA, sgolpe, animaciones)
	jugadores.add(j)


	#Animacion enemigo 1
	aniene1 = ani.aniEnemigo1()
	#Animacion enemigo 2
	aniene2 = ani.aniEnemigo2()

	# Diferencial por la posicion inicial del fondo cuando carga la pantalla
	diffFondo = cnt.ALTO- alto_fondo

	
	#Posicion y velocidad de la "camara o pantalla" 
	f_x = 0
	f_velx = 0
	f_y = diffFondo
	f_vely = 0

	inicializarcolliders(j.blockers, j.triggers, diffFondo)

	"""Creacion de objetos"""
	imgvida = pg.image.load('Sprites/vida.png')
	imgpower = pg.image.load('Sprites/power.png')
	imgvelatk = pg.image.load('Sprites/velatk.png')

	#Objeto al lado de la choza
	ob = obj.Modificador(imgpower, "power", [688, 160], jugadores, objetosG)
	objetosG.add(ob)
	movergrupoobjetos(0, diffFondo)

	# ---------------------------------------
	finalboss = True
	vivo = False
	# ---------------------------------------
	listaPE = []
	#Posicion enemigos choza1
	pec1 = [576, 194]
	enmcz1 = 2
	pec2 = [2721, 129]
	tempChoza = 0
	listaPE.append(pec1)
	listaPE.append(pec2)

	# Chocitas
	tempChocita = 0
	contPE = []
	contPE = ch.generateCantPE(contPE)
	imgchocita = pg.image.load('Sprites/chocita.png')
	listachocitas = []
	
	listachocitas = ch.getChocitas(listachocitas)
	listaPE = ch.getPosPE(listaPE)

	listachocitas = moverlist_ene_cho(listachocitas, 0, diffFondo)
	listaPE = moverlist_ene_cho(listaPE, 0, diffFondo)

	j.chocitas = listachocitas
	#print(j.blockers[0])
	#j.blockers[0][1] = j.blockers[0][1] + 30 
	#print(j.blockers[0])

	# Interfaz
	fuente=pg.font.Font(None,32)

	#Sonido
	sonidofondo = pg.mixer.Sound('Sprites/Sonido/fondo.ogg')
	sonidofondo.set_volume(0.2)
	sonidofondo.play()

	fin_juego=False

	fps_clock = pg.time.Clock()
	while(True and (not fin_juego and j.finalboss)):
		keys = pg.key.get_pressed()
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_LEFT:
					j.dir = 1
					j.velx = -2
					j.vely = 0
					f_velx = 2
					f_vely = 0

				if event.key == pg.K_RIGHT:
					j.dir = 0
					j.velx = 2
					j.vely = 0
					f_velx = -2
					f_vely = 0

				if event.key == pg.K_DOWN:
					j.dir = 3
					j.velx = 0
					j.vely = 2
					f_vely = -2
					f_velx = 0

				if event.key == pg.K_UP:
					j.dir = 2
					j.velx = 0
					j.vely = -2
					f_vely = 2
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

		
		if (j.salud <= 0):
			fin_juego = True

		# Control mapa y colisiones
		if(j.rect.x > (cnt.ANCHO-150) and f_x > (cnt.ANCHO-ancho_fondo) 
			and f_velx < 0):
			f_x += f_velx
			movercolliders(j.blockers, j.triggers, f_velx, 0)
			movergrupoenemigos(f_velx, 0)
			movergrupoobjetos(f_velx, 0)
			moverlist_ene_cho(listachocitas, f_velx, 0)
			moverlist_ene_cho(listaPE, f_velx, 0)
			j.velx = 0 

		if(j.rect.x < 150 and f_x < 0 and f_velx > 0):
			f_x += f_velx
			movercolliders(j.blockers, j.triggers, f_velx, 0)
			movergrupoenemigos(f_velx, 0)
			movergrupoobjetos(f_velx, 0)
			moverlist_ene_cho(listachocitas, f_velx, 0)
			moverlist_ene_cho(listaPE, f_velx, 0)
			j.velx = 0 

		if(j.rect.y > (cnt.ALTO-150) and f_y > (cnt.ALTO-alto_fondo)
			and f_vely < 0):
			f_y += f_vely
			movercolliders(j.blockers, j.triggers, 0, f_vely)
			movergrupoenemigos(0, f_vely) 
			movergrupoobjetos(0, f_vely)
			moverlist_ene_cho(listachocitas, 0, f_vely)
			moverlist_ene_cho(listaPE, 0, f_vely)
			j.vely = 0 

		if(j.rect.y < 150 and f_y < 0 and f_vely > 0):
			f_y += f_vely
			movercolliders(j.blockers, j.triggers, 0, f_vely)
			movergrupoenemigos(0, f_vely)
			movergrupoobjetos(0, f_vely)
			moverlist_ene_cho(listachocitas, 0, f_vely)
			moverlist_ene_cho(listaPE, 0, f_vely) 
			j.vely = 0      


		#Control enemigo
		if(j.zone and (not enemigosA) and (tempChoza == 250) and j.zoneName == "choza1" and enmcz1 > 0):
			#objeto enemigo A
			e = pj.EnemigoA(blockers, triggers, pec1, j, aniene1)
			enemigosA.add(e)
			j.zone = False
			tempChoza = 0
			enmcz1-=1

		if(j.zone and (tempChoza == 250) and j.zoneName == "choza2"):
			if(finalboss):
				e = pj.EnemigoB(blockers, triggers, pec2, j, aniene2)
				enemigosA.add(e)
				j.zone = False
				tempChoza = 0

		if((not enemigosA) and (tempChoza < 250)):
			tempChoza+=1


		# generacion enemigos en chocita2
		if(j.zone and j.zoneName == "chocita2"):
			if(listachocitas[1]):
				chozax = listachocitas[1][0]
				chozay = listachocitas[1][1] +1
			if(j.golpechoza):
				listachocitas[1] = False
				j.golpechoza = False
				crearModificador([chozax+10, chozay+10])

			if(contPE[1] > 0 and (tempChocita == 200) and listachocitas[1]):
				print("Creado ch2")
				e = pj.EnemigoA(blockers, triggers, listaPE[3], j, aniene1)
				enemigosA.add(e)
				j.zone = False
				tempChocita = 0
				contPE[1] -= 1

			for blocker in j.blockers:
				eqlx = blocker.x == chozax
				eqly = blocker.y == chozay
				if j.rect.colliderect(blocker) and eqlx and eqly:
					j.choquecho = True
					if(not listachocitas[1]):
						j.blockers.remove(blocker)
						j.choquecho = False
					


		# generacion enemigos en chocita1
		if(j.zone and j.zoneName == "chocita1"):
			if(listachocitas[0]):
				chozax = listachocitas[0][0] + 1
				chozay = listachocitas[0][1] + 21
			if(j.golpechoza):
				listachocitas[0] = False
				j.golpechoza = False
				crearModificador([chozax+10, chozay+10])

			if(contPE[0] > 0 and (tempChocita == 200) and listachocitas[0]):
				print("Creado ch1")
				e = pj.EnemigoA(blockers, triggers, listaPE[2], j, aniene1)
				enemigosA.add(e)
				j.zone = False
				tempChocita = 0
				contPE[0] -= 1

			for blocker in j.blockers:
				eqlx = blocker.x == chozax
				eqly = blocker.y == chozay
				#if j.rect.colliderect(blocker):
					#print("blocker", blocker.x, blocker.y)
					#print("choci", chozax, chozay)
				if j.rect.colliderect(blocker) and eqlx and eqly:
					j.choquecho = True
					if(not listachocitas[0]):
						j.blockers.remove(blocker)
						j.choquecho = False


			# generacion enemigos en chocita3
		if(j.zone and j.zoneName == "chocita3"):
			if(listachocitas[2]):
				chozax = listachocitas[2][0]
				chozay = listachocitas[2][1] + 9
			if(j.golpechoza):
				listachocitas[2] = False
				j.golpechoza = False
				crearModificador([chozax+10, chozay+10])

			if(contPE[2] > 0 and (tempChocita == 200) and listachocitas[2]):
				print("Creado ch1")
				e = pj.EnemigoA(blockers, triggers, listaPE[4], j, aniene1)
				enemigosA.add(e)
				j.zone = False
				tempChocita = 0
				contPE[2] -= 1

			for blocker in j.blockers:
				eqlx = blocker.x == chozax
				eqly = blocker.y == chozay
				#if j.rect.colliderect(blocker):
				#	print("blocker", blocker.x, blocker.y)
				#	print("choci", chozax, chozay)
				if j.rect.colliderect(blocker) and eqlx and eqly:
					j.choquecho = True
					if(not listachocitas[2]):
						j.blockers.remove(blocker)
						j.choquecho = False
					


		if(tempChocita < 200):
			tempChocita+=1


		#HUD
		info_salud='Salud: ' + str(j.salud)
		info_pow='Poder: ' + str(j.powatk)
		info_vel='Vel Ataque: ' + str(j.velatk)
		texto=fuente.render(info_salud,True, cnt.AMARILLO)
		texto1=fuente.render(info_pow,True, cnt.AMARILLO)
		texto2=fuente.render(info_vel,True, cnt.AMARILLO)
			
		# Actualizar pantalla
		pantalla.blit(map_surface, [f_x,f_y])
		printchocitas(pantalla, imgchocita, listachocitas)

		objetosG.update()
		objetosG.draw(pantalla)

		enemigosA.update()
		enemigosA.draw(pantalla)

		jugadores.update(keys)
		jugadores.draw(pantalla)
		

		pantalla.blit(texto,[50,30])
		pantalla.blit(texto1,[200,30])
		pantalla.blit(texto2,[350,30])

		pg.display.update()
		fps_clock.tick(60)



	sonidofondo.stop()
	if(cnt.WIN):
		#pantalla de fin de juego victoria
		imgfin = pg.image.load('Sprites/winim.png')
		fin = False
		while not fin:
		        #gestion de eventos
		        for event in pg.event.get():
		            if event.type == pg.QUIT:
		                fin=True

		        pantalla.fill(cnt.BLANCO)
		        pantalla.blit(imgfin,[250,100])
		        pg.display.flip()

	else:
		#pantalla de fin de juego
		imgfin = pg.image.load('Sprites/finjuego.png')
		fin = False
		while not fin:
		        #gestion de eventos
		        for event in pg.event.get():
		            if event.type == pg.QUIT:
		                fin=True

		        pantalla.fill(cnt.NEGRO)
		        pantalla.blit(imgfin,[-70,-25])
		        pg.display.flip()
	 