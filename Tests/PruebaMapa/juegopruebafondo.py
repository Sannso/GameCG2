import pygame
import pytmx

#850×480
ANCHO=850   #x4 = 3400
ALTO=480    #x3 = 1440


class BackgroundLayer():
    def __init__(self):
        self.gameMap = pytmx.load_pygame("tiledmapa.tmx")
        self.layer1 = self.gameMap['Pasto']
        self.layer2 = self.gameMap['Terreno']
        self.layer3 = self.gameMap['Objetos']
        self.layer4 = self.gameMap['SobrePersonaje']

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    
    background = BackgroundLayer()

    clock = pygame.time.Clock()
    fin=False
    while(True):
        clock.tick(60)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                quit()

        for layer in background.gameMap.visible_layers:
                for x, y, gid, in layer:
                    tile = background.gameMap.get_tile_image_by_gid(gid)
                    if(tile != None):
                        display.blit(tile, (x * background.gameMap.tilewidth, y * background.gameMap.tileheight))
        pygame.display.flip()