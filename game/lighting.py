import pygame
from wizard import Wizard


GROUND = 500






class Lighting(pygame.sprite.Sprite):

    
    def __init__ (self, win, wiz, x, y, cy, cx, *groups):
        super().__init__(*groups)

        self.wiz = wiz
        self.win = win
        self.x = x
        self.y = y
        self.cy = cy
        self.cx = cx


        self.cloud = pygame.image.load("..\\sprites\\cloud.png")
        self.rect = self.cloud.get_rect(topleft=(self.cx, cy))
        

        self.image = pygame.image.load("..\\sprites\\lighting.png")
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        
    def update(self):
        
        if (self.y <= GROUND):
            self.y += 0.2
            
            
            self.win.blit(self.cloud, (self.cx, self.cy))
            self.win.blit(self.image, (self.x, self.y))
        else:
            self.kill()

        
            
        
        

        

