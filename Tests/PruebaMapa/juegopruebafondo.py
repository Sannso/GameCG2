import pygame
import pytmx
import random

#850×480
ANCHO=850   #x4 = 3400
ALTO=480    #x3 = 1440



VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
AMARILLO=[255,255,0]
AZUL_2=[0,255,255]
NEGRO=[0,0,0]
BLANCO=[255,255,255]
GRIS=[180,180,180]

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(AMARILLO)
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=250
        self.velx=0
        self.vely=0
        self.salud=200
        self.bloques=[]
        self.ratones=[]

    def update(self):

        ls_obj = pygame.sprite.spritecollide(self,self.bloques,False)
        for b in ls_obj:
            if self.rect.right > b.rect.left and self.velx>0 :
                self.rect.right = b.rect.left
                self.velx=0

            if self.rect.left < b.rect.right and self.velx<0:
                self.rect.left = b.rect.right
                self.velx=0

            if self.rect.bottom > b.rect.top and self.vely>0:
                self.rect.bottom = b.rect.top
                self.vely=0

            if self.rect.top < b.rect.bottom and self.vely<0:
                self.rect.top = b.rect.bottom
                self.vely=0

        self.rect.x+=self.velx
        self.rect.y+=self.vely


class BackgroundLayer():
    def __init__(self):
        self.gameMap = pytmx.load_pygame("tiledmapa.tmx", pixelalpha=True)
        self.layer1 = self.gameMap.get_layer_by_name('Pasto')
        self.layer2 = self.gameMap.get_layer_by_name('Terreno')
        self.layer3 = self.gameMap.get_layer_by_name('Objetos')
        #self.layer4 = self.gameMap['SobrePersonaje']

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    #crear
    jugadores=pygame.sprite.Group()

    #objeto jugador
    j=Jugador()
    jugadores.add(j)

    f_x=0
    f_velx=0
    f_y=0
    f_vely=0
    
    background = BackgroundLayer()
    for x, y, gid in background.layer1:
            tile = background.gameMap.get_tile_image_by_gid(gid)
            print(x, y, gid)
            if tile:
                pantalla.blit(tile, (x * background.gameMap.tilewidth, y * background.gameMap.tileheight))
    for x, y, gid in background.layer2:
            tile = background.gameMap.get_tile_image_by_gid(gid)
            print(x, y, gid)
            if tile:
                pantalla.blit(tile, (x * background.gameMap.tilewidth, y * background.gameMap.tileheight))
    for x, y, gid in background.layer3:
            tile = background.gameMap.get_tile_image_by_gid(gid)
            print(x, y, gid)
            if tile:
                pantalla.blit(tile, (x * background.gameMap.tilewidth, y * background.gameMap.tileheight))

    clock = pygame.time.Clock()
    fin=False
    while(True):
        
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    j.velx = -5
                    j.vely = 0
                    f_velx = 5
                    f_vely = 0

                if event.key == pygame.K_RIGHT:
                    j.velx = 5
                    j.vely = 0
                    f_velx = -5
                    f_vely = 0

                if event.key == pygame.K_DOWN:
                    j.velx = 0
                    j.vely = 5
                    f_vely = -5
                    f_velx = 0

                if event.key == pygame.K_UP:
                    j.velx = 0
                    j.vely = -5
                    f_vely = 5
                    f_velx = 0

            if event.type == pygame.KEYUP:
                if (((event.key == pygame.K_LEFT) and (j.velx < 0))
                 or ((event.key == pygame.K_RIGHT) and (j.velx > 0))):
                    j.velx = 0
                    

                if (((event.key == pygame.K_DOWN) and (j.vely > 0))
                 or ((event.key == pygame.K_UP) and (j.vely < 0))):
                    j.vely = 0

                if (((event.key == pygame.K_LEFT) and (f_velx > 0))
                 or ((event.key == pygame.K_RIGHT) and (f_velx < 0))):
                    f_velx = 0

                if (((event.key == pygame.K_DOWN) and (f_vely < 0))
                 or ((event.key == pygame.K_UP) and (f_vely > 0))):
                    f_vely = 0
                    

        # Control

        if(j.rect.x > (ANCHO-150) and f_x > (ANCHO-ancho_fondo) 
            and f_velx < 0):
            f_x += f_velx
            j.velx = 0 

        if(j.rect.x < 150 and f_x < 0 and f_velx > 0):
            f_x += f_velx
            j.velx = 0 

        if(j.rect.y > (ALTO-150) and f_y > (ALTO-alto_fondo)
            and f_vely < 0):
            f_y += f_vely 
            j.vely = 0 

        if(j.rect.y < 150 and f_y < 0 and f_vely > 0):
            f_y += f_vely
            j.vely = 0      


        # Actualizar pantalla
        jugadores.update()
        jugadores.draw(pantalla)

        pygame.display.flip()
        clock.tick(30)