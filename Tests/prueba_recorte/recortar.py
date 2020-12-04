import pygame
import random



def Recortar(list_cuadritos, imagen, objetos_ancho, objetos_alto):
    terreno=pygame.image.load(imagen)
    info=terreno.get_rect()
    print (info)
    #parametros: posicion x, posicion y, ancho corte, alto corte
    an_t=info[2]
    al_t=info[3]
    print (an_t, al_t)
    ob_an = objetos_ancho
    ob_al = objetos_alto

    an_sp = an_t / ob_an
    al_sp = al_t / ob_al
    print ('ancho sprite: ', an_sp)
    print ('alto sprite: ', al_sp)
    ls_cuadro=[]
    list_cuadritos=[]
   
    for fila in range(ob_al):
        for col in range(ob_an):
            cuadro=terreno.subsurface(col*an_sp,fila*al_sp,an_sp,al_sp)
            ls_cuadro.append(cuadro)
        list_cuadritos.append(ls_cuadro.copy())
        ls_cuadro.clear()


    return list_cuadritos    
