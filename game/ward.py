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
        
         

        self.dodgeIncrease = 1.25

        self.oldDodge_chance = wiz.get_dodge_chance()

        self.ward = pygame.image.load("..\\sprites\\ward.png") #TODO \change/ done
        self.wardHB = self.ward.get_rect(topleft=(800, 200))

        
    
    def dodgeUp(self, wiz):
        if (wiz.is_ward == False):
            self.newDodge_chance = self.oldDodge_chance * self.dodgeIncrease
            wiz.set_dodge_chance(self.newDodge_chance)
            wiz.is_ward = True

    def update(self, win, wiz):
        self.elapsed_time = time.time() - self.start_time 
        if (self.elapsed_time < 2.0):

            self.win.blit(self.ward,(800, 200))
        
        else:
            self.kill

        


