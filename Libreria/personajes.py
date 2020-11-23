import pygame
import Libreria.constantes as cnt

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(cnt.AMARILLO)
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=250
        self.velx=0
        self.vely=0
        self.salud=200

    def update(self):

        self.rect.x+=self.velx
        self.rect.y+=self.vely