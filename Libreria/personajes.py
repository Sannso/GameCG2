import pygame
import Libreria.constantes as cnt

class Jugador(pygame.sprite.Sprite):
    def __init__(self, blockers, triggers, blockerpjs, eneA, sonido, animaciones):
        pygame.sprite.Sprite.__init__(self)
        self.animaciones = animaciones
        self.dir = 0
        self.con = 0
        self.image = self.animaciones[self.dir][self.con]
        self.estado = 0
        self.rect=self.image.get_rect()
        self.rect.x= 60
        self.rect.y= cnt.ALTO - 275
        self.velx=0
        self.vely=0
        self.salud=60
        self.blockers = blockers
        self.blockerpjs = blockerpjs
        self.triggers = triggers
        self.enemigosA = eneA
        self.zone = False
        self.zoneName = ""
        self.velatk = 60
        self.powatk = 15
        self.auxvel = self.velatk
        self.choquecho = False
        self.golpechoza = False
        self.finalboss = True
        self.sonido = sonido

    def update(self, keys):

        if(self.auxvel == 0 and keys[pygame.K_z]):
            self.auxvel = self.velatk
            self.sonido.play()
            self.estado = 1
            if(self.enemigosA):
                collide = pygame.sprite.spritecollide(self,self.enemigosA,False)
                if(collide):
                    collide[0].salud -= self.powatk
                    if(collide[0].salud <= 0):
                        if(collide[0].velatk == 140):
                            self.finalboss = False
                            cnt.WIN = True
                        collide[0].remove(self.enemigosA)

            if(self.choquecho):
                self.choquecho = False
                self.golpechoza = True
                
        elif(self.auxvel > 0):
            self.auxvel-=1


        self.rect.x += self.velx
        self.rect.y += self.vely


        if self.estado == 0 and (self.velx != 0 or self.vely != 0):

            self.image = self.animaciones[self.dir][self.con]
            if self.con < 3:
                self.con += 1
            else:
                self.con = 0
        elif self.estado == 1:
            if self.dir == 0:
                self.image = self.animaciones[4][self.con]
            elif self.dir == 1:
                self.image = self.animaciones[5][self.con]
            elif self.dir == 2:
                pass
            elif self.dir == 3:
                self.image = self.animaciones[6][self.con]

            if self.con < 3:
                self.con += 1
            else:
                self.con = 0
                self.estado = 0


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
                #print(trigger)
                if(trigger[2] == 163 and trigger[3] == 181):
                    self.zoneName = "chocita2"

                if(trigger[2] == 161 and trigger[3] == 212):
                    self.zoneName = "chocita1"

                if(trigger[2] == 155 and trigger[3] == 114):
                    self.zoneName = "chocita3"

                if(trigger[2] == 440 and trigger[3] == 376):
                    self.zoneName = "choza1"

                if(trigger[2] == 612 and trigger[3] == 422):
                    self.zoneName = "choza2"
                   

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)



class EnemigoA(pygame.sprite.Sprite):
    def __init__(self, blockers, triggers, pos, jugador, animaciones):
        self.animaciones = animaciones
        self.dir = 0
        self.con = 0
        self.image = self.animaciones[self.dir][self.con]
        pygame.sprite.Sprite.__init__(self)
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
        self.velatk = 90
        self.auxvel = 10

    def update(self):

        diffX = abs(self.player.rect.x - self.rect.x) > 10
        diffY = abs(self.player.rect.y - self.rect.y) > 10

        if(self.player.zone):
            if((not diffX) and  (not diffY)):
                self.velx = 0
                self.vely = 0
                self.atacar = True
            elif(((self.player.rect.x-10 > self.rect.x) or (self.player.rect.x > self.rect.x)) and diffX):
                self.dir = 0
                self.velx = 2
                self.vely = 0
                self.atacar = False
            elif(((self.player.rect.x-10 < self.rect.x) or (self.player.rect.x < self.rect.x))  and diffX):
                self.dir = 1
                self.velx = -2
                self.vely = 0
                self.atacar = False
            elif(((self.player.rect.y-10 > self.rect.y) or (self.player.rect.y > self.rect.y))  and diffY):
                self.dir = 3
                self.vely = 2
                self.velx = 0
                self.atacar = False
            elif(((self.player.rect.y-10 < self.rect.y) or (self.player.rect.y < self.rect.y))  and diffY):
                self.dir = 2
                self.vely = -2
                self.velx = 0
                self.atacar = False

        if(self.velx != 0 or self.vely != 0):
            self.image = self.animaciones[self.dir][self.con]
            if self.con < 3:
                self.con += 1
            else:
                self.con = 0

        if(self.atacar):
            if(self.auxvel == 0):
                self.player.salud -= 10
                self.auxvel = self.velatk
            else:
                self.auxvel-=1

        self.rect.x += self.velx
        self.rect.y += self.vely
     
            

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)


class EnemigoB(pygame.sprite.Sprite):
    def __init__(self, blockers, triggers, pos, jugador, animaciones):
        self.animaciones = animaciones
        self.dir = 0
        self.con = 0
        self.image = self.animaciones[self.dir][self.con]
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([35,40])
        self.image.fill(cnt.AZUL)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.salud=100
        self.blockers = blockers
        self.triggers = triggers
        self.player = jugador
        self.atacar = False
        self.velatk = 140
        self.auxvel = 10

    def update(self):

        diffX = abs(self.player.rect.x - self.rect.x) > 10
        diffY = abs(self.player.rect.y - self.rect.y) > 10

        if(self.player.zone):
            if((not diffX) and  (not diffY)):
                self.velx = 0
                self.vely = 0
                self.atacar = True
            elif(((self.player.rect.x-10 > self.rect.x) or (self.player.rect.x > self.rect.x)) and diffX):
                self.dir = 0
                self.velx = 1
                self.vely = 0
                self.atacar = False
            elif(((self.player.rect.x-10 < self.rect.x) or (self.player.rect.x < self.rect.x))  and diffX):
                self.dir = 1
                self.velx = -1
                self.vely = 0
                self.atacar = False
            elif(((self.player.rect.y-10 > self.rect.y) or (self.player.rect.y > self.rect.y))  and diffY):
                self.dir = 3
                self.vely = 1
                self.velx = 0
                self.atacar = False
            elif(((self.player.rect.y-10 < self.rect.y) or (self.player.rect.y < self.rect.y))  and diffY):
                self.dir = 2
                self.vely = -1
                self.velx = 0
                self.atacar = False

        if(self.velx != 0 or self.vely != 0):
            self.image = self.animaciones[self.dir][self.con]
            if self.con < 3:
                self.con += 1
            else:
                self.con = 0

        if(self.atacar):
            if(self.auxvel == 0):
                self.player.salud -= 30
                self.auxvel = self.velatk
            else:
                self.auxvel-=1

        self.rect.x += self.velx
        self.rect.y += self.vely
     
            

    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)