import pygame
from wizard import Wizard


class Ward(pygame.sprite.Sprite):
    '''
    class for running Ward(to make the dogde chance greater using a spell)
    '''
    self.wiz = wiz
    if (wiz.is_wizard == False):

    def __init__(self, wiz):
        
        
        self.image = pygame.image.load("..\\sprites\\wizard.png") #TODO change

        self.dodgeIncrease = 1.25

        self.oldDodge_chance = wiz.get_dodge_chance()

        
    
    def dodgeUp(self, wiz):
        if (wiz.is_ward == False):
            self.newDodge_chance = self.oldDodge_chance * self.dodgeIncrease
            wiz.set_dodge_chance(self.newDodge_chance)
            wiz.is_ward = True

        


