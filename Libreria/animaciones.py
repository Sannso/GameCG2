import Libreria.recorte as r



def aniPrincipal():
	nombre_der = 'Sprites/personaje/derecha.png'
	nombre_izq = 'Sprites/personaje/izquierda.png'
	nombre_arriba = 'Sprites/personaje/arriba.png'
	nombre_abajo = 'Sprites/personaje/frente.png'
	atacando_der = 'Sprites/personaje/atkderecha.png'
	atacando_izq = 'Sprites/personaje/atkizquierda.png'
	atacando_abajo = 'Sprites/personaje/atkabajo.png'
	ancho_imagen = 4
	alto_imagen = 1

	r.recortar_imagen(nombre_der, ancho_imagen, alto_imagen,0)
	r.recortar_imagen(nombre_izq, ancho_imagen, alto_imagen,1)
	r.recortar_imagen(nombre_arriba, ancho_imagen, alto_imagen,2)
	r.recortar_imagen(nombre_abajo, ancho_imagen, alto_imagen,3)
	r.recortar_imagen(atacando_der, ancho_imagen, alto_imagen, 4)
	r.recortar_imagen(atacando_izq, ancho_imagen, alto_imagen, 5)
	r.recortar_imagen(atacando_abajo, ancho_imagen, alto_imagen, 6) 

	result = r.animapersonaje.copy()
	r.animapersonaje.clear()
	return result


def aniEnemigo1():
	nombre_der = 'Sprites/enemigo1/derecha.png'
	nombre_izq = 'Sprites/enemigo1/izquierda.png'
	nombre_arriba = 'Sprites/enemigo1/arriba.png'
	nombre_abajo = 'Sprites/enemigo1/abajo.png'
	atacando_der = 'Sprites/enemigo1/atkderecha.png'
	atacando_izq = 'Sprites/enemigo1/atkizquierda.png'
	atacando_abajo = 'Sprites/enemigo1/atkabajo.png'
	ancho_imagen = 4
	alto_imagen = 1

	r.recortar_imagen(nombre_der, ancho_imagen, alto_imagen,0)
	r.recortar_imagen(nombre_izq, ancho_imagen, alto_imagen,1)
	r.recortar_imagen(nombre_arriba, ancho_imagen, alto_imagen,2)
	r.recortar_imagen(nombre_abajo, ancho_imagen, alto_imagen,3)
	r.recortar_imagen(atacando_der, ancho_imagen, alto_imagen, 4)
	r.recortar_imagen(atacando_izq, ancho_imagen, alto_imagen, 5)
	r.recortar_imagen(atacando_abajo, ancho_imagen, alto_imagen, 6) 

	result = r.animapersonaje.copy()
	r.animapersonaje.clear()
	return result


def aniEnemigo2():
	nombre_der = 'Sprites/enemigo2/derecha.png'
	nombre_izq = 'Sprites/enemigo2/izquierda.png'
	nombre_arriba = 'Sprites/enemigo2/arriba.png'
	nombre_abajo = 'Sprites/enemigo2/abajo.png'
	ancho_imagen = 6
	alto_imagen = 1

	r.recortar_imagen(nombre_der, ancho_imagen, alto_imagen,0)
	r.recortar_imagen(nombre_izq, ancho_imagen, alto_imagen,1)
	r.recortar_imagen(nombre_arriba, 9, 1,2)
	r.recortar_imagen(nombre_abajo, 9, 1,3)

	result = r.animapersonaje.copy()
	r.animapersonaje.clear()
	return result