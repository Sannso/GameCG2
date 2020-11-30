import pygame
import Libreria.constantes as cnt

class Jugador(pygame.sprite.Sprite):
    def __init__(self, blockers, triggers, eneA):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([50,50])
        self.image.fill(cnt.AMARILLO)
        self.rect=self.image.get_rect()
        self.rect.x= 60
        self.rect.y= cnt.ALTO - 275
        self.velx=0
        self.vely=0
        self.salud=50
        self.blockers = blockers
        self.triggers = triggers
        self.enemigosA = eneA
        self.zone = False

    def update(self, keys):

        self.rect.x += self.velx
        self.rect.y += self.vely
        for blocker in self.blockers:

            if self.rect.colliderect(blocker) and (self.velx >= 0 and self.vely == 0) and keys[pygame.K_RIGHT]:
                self.rect.right = blocker.left
                self.velx = 0

            elif self.rect.colliderect(blocker) and (self.velx <= 0 and self.vely == 0) and keys[pygame.K_LEFT]:
                self.rect.left = blocker.right
                self.velx = 0

            elif self.rect.colliderect(blocker) and (self.vely >= 0 and self.velx == 0) and keys[pygame.K_DOWN]:
                self.rect.bottom = blocker.top
                self.vely = 0

            elif self.rect.colliderect(blocker) and (self.vely <= 0 and self.velx == 0) and keys[pygame.K_UP]:
                self.rect.top = blocker.bottom
                self.vely = 0

        for trigger in self.triggers:
            if self.rect.colliderect(trigger):
                self.zone = True
                   

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)



class EnemigoA(pygame.sprite.Sprite):
    def __init__(self, blockers, triggers, pos, jugador):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([35,40])
        self.image.fill(cnt.AZUL)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.salud=30
        self.blockers = blockers
        self.triggers = triggers
        self.player = jugador
        self.atacar = False
        self.velatk = 10

    def update(self):

        diffX = abs(self.player.rect.x - self.rect.x) > 10
        diffY = abs(self.player.rect.y - self.rect.y) > 10

        if(self.player.zone):
            if((not diffX) and  (not diffY)):
                self.velx = 0
                self.vely = 0
                self.atacar = True
            elif(((self.player.rect.x-10 > self.rect.x) or (self.player.rect.x > self.rect.x)) and diffX):
                self.velx = 2
                self.vely = 0
            elif(((self.player.rect.x-10 < self.rect.x) or (self.player.rect.x < self.rect.x))  and diffX):
                self.velx = -2
                self.vely = 0
            elif(((self.player.rect.y-10 > self.rect.y) or (self.player.rect.y > self.rect.y))  and diffY):
                self.vely = 2
                self.velx = 0
            elif(((self.player.rect.y-10 < self.rect.y) or (self.player.rect.y < self.rect.y))  and diffY):
                self.vely = -2
                self.velx = 0

        self.rect.x += self.velx
        self.rect.y += self.vely
     
            

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)