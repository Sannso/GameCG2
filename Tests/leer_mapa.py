import pygame
import configparser

#850×480
ANCHO=850   #x4 = 3400
ALTO=480    #x3 = 1440

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    archivo=configparser.ConfigParser()
    archivo.read('info_mapa.txt')
    nom_imagen=archivo.get('info','imagen')
    terreno=pygame.image.load(nom_imagen)
    info=terreno.get_rect()

    an_t=info[2]
    al_t=info[3]

    ob_an= int (archivo.get('info','can_ancho'))
    ob_al= int (archivo.get('info','can_alto'))

    an_sp = int(an_t / ob_an)
    al_sp = int(al_t / ob_al)
    print ('ancho sprite: ',an_t / ob_an)
    print ('alto sprite: ', al_t / ob_al)

    ls_cuadro=[]
    ls_terreno=[]
   
    for fila in range(ob_al):
        for col in range(ob_an):
            cuadro=terreno.subsurface(col*an_sp,fila*al_sp,an_sp,al_sp)
            ls_cuadro.append(cuadro)
        ls_terreno.append(ls_cuadro.copy())
        ls_cuadro.clear() 


    mapa=archivo.get('info','mapa')
    ls_filas=mapa.split('\n')
    print(ls_filas)
    con=0
    con_fil=0
    for e in ls_filas:
        for j in e:     
            col=int(archivo.get(j,'col'))
            fila=int(archivo.get(j,'fil'))
            pantalla.blit(ls_terreno[fila][col],[con*an_sp,con_fil*al_sp])
            con+=1
        con_fil+=1
        con = 0

    #pantalla.blit(ls_t[0],[0,0])
    pygame.display.flip()
    fin=False
    while not fin :
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
