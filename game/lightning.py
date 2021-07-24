import pygame
from wizard import Wizard


GROUND = 500






class Lightning(pygame.sprite.Sprite):

    
    def __init__ (self, win, wiz, x, y, cy, cx, *groups):
        super().__init__(*groups)

        self.wiz = wiz
        self.win = win
        self.x = x
        self.y = y
        self.cy = cy
        self.cx = cx


        self.cloud = pygame.image.load("..\\sprites\\cloud.png")
        #self.rect = self.cloud.get_rect(topleft=(self.cx, cy))
        self.rect = self.cloud.get_rect()
        self.win.blit(self.cloud, (self.cx, self.cy))
        
        self.image = pygame.image.load("..\\sprites\\lightning.png")
        #self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.rect = self.image.get_rect()

        
    def update(self):
        print(self.cx)
        print(self.cy)
        if (self.y <= GROUND):
            self.y += 0.2
            
            self.cy += 0.0000001
            self.win.blit(self.cloud, (self.cx, self.cy))
            self.win.blit(self.image, (self.x, self.y))
            

        else:
            self.kill()

        
            
        
        

        

