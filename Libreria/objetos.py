import pygame
import Libreria.constantes as cnt

class Modificador(pygame.sprite.Sprite):
    def __init__(self, image, name, pos, personaje, owngp):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect=self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.name = name
        self.player = personaje
        self.grupoobj = owngp
       

    def update(self):
    	if(self.name == "vida"):
    		if(self.player):
    			collide = pygame.sprite.spritecollide(self,self.player,False)
    			if(collide):
    				collide[0].salud = 60
    				self.remove(self.grupoobj)


    	if(self.name == "velatk"):
    		if(self.player):
	        	collide = pygame.sprite.spritecollide(self,self.player,False)
	        	if(collide):
	        		collide[0].velatk -= 20
	        		if(collide[0].velatk < 0):
	        			collide[0].velatk = 0
	        		self.remove(self.grupoobj)


    	if(self.name == "power"):
	        if(self.player):
	                collide = pygame.sprite.spritecollide(self,self.player,False)
	                if(collide):
	                    collide[0].powatk += 30
	                    self.remove(self.grupoobj)


		 