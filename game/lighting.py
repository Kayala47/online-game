import pygame
from wizard import Wizard


GROUND = 500






class Lighting(pygame.sprite.Sprite):

    
    def __init__ (self, win, wiz, x, y, *groups):
        super().__init__(*groups)

        self.wiz = wiz
        self.win = win
        self.x = x
        self.y = y


        self.cloud = pygame.image.load("..\\sprites\\cloud.png")
        

        self.image = pygame.image.load("..\\sprites\\lighting.png")
        self.rect = self.cloud.get_rect(topleft=(self.x, self.y))

        self.win.blit(self.cloud, (self.x, self.y))
    def update(self):
        if (self.y <= GROUND):
            self.y += 1
            print(self.y)
            
            self.win.blit(self.image, (self.x, self.y))
        else:
            self.kill()

        
            
        
        

        

