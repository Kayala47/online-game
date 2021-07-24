import pygame
import time
from wizard import Wizard


GROUND = 500






class Lightning(pygame.sprite.Sprite):

    
    def __init__ (self, win, wiz, x, y, *groups):
        super().__init__(*groups)

        self.wiz = wiz
        self.win = win
        self.x = x
        self.y = y


        
        
        self.image = pygame.image.load("..\\sprites\\lightning.png")
        #self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.rect = self.image.get_rect()

        
    def update(self):
       
        if (self.y <= GROUND):
            self.y += 0.2
            
           
            
            self.win.blit(self.image, (self.x, self.y))
            

        else:
            self.kill()

class Cloud(pygame.sprite.Sprite):

    
    def __init__ (self, win, wiz, x, y, *groups):
        super().__init__(*groups)

        self.wiz = wiz
        self.win = win
        self.x = x
        self.y = y
        self.start_time = time.time()
        


        self.cloud = pygame.image.load("..\\sprites\\cloud.png")
        #self.rect = self.cloud.get_rect(topleft=(self.cx, cy))
        self.rect = self.cloud.get_rect()
        self.win.blit(self.cloud, (self.x, self.y))
        


        
    def update(self):
        self.elapsed_time = time.time() - self.start_time
        if (self.elapsed_time < 1.7):
            
            
            
            self.win.blit(self.cloud, (self.x, self.y))
            
            

        else:
            self.kill()
            

        
            
        
        

