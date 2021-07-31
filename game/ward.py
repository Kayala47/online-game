import pygame
import time
from wizard import Wizard


class Ward(pygame.sprite.Sprite):
    '''
    class for running Ward(to make the dogde chance greater using a spell)
    '''
    
    def __init__(self, wiz, win,  *groups):
        super().__init__(*groups)
        self.wiz = wiz
        self.win = win
        self.start_time = time.time()
        self.round = 0
         

        self.dodgeIncrease = 1.25
        self.oldDodge_chance = wiz.get_dodge_chance()
        

        self.ward = pygame.image.load("..\\sprites\\ward.png")
        self.wardHB = self.ward.get_rect(topleft=(800, 200))
        self.height = self.wardHB.height
        if (wiz.is_ward == False):
            self.dodgeUp(wiz)
            self.wiz.set_ward(True)
        
    
    def dodgeUp(self, wiz):
        if (wiz.is_ward == False):
            print(self.oldDodge_chance)
            self.newDodge_chance = self.oldDodge_chance * self.dodgeIncrease
            wiz.set_dodge_chance(self.newDodge_chance)
            print(self.newDodge_chance)
            
    def dodgeDown(self):
        self.wiz.set_dodge_chance(self.oldDodge_chance)

    def update(self):
        self.round += 1
        print(self.round)
        self.elapsed_time = time.time() - self.start_time 
        self.x, self.y = self.wiz.get_position()
        self.y -= self.height
        if (self.round < 2):

            self.win.blit(self.ward,(self.x, self.y))
        
        else:
            self.wiz.set_ward(False)
            self.dodgeDown()
            self.kill()
        
            

        


