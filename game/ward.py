import pygame
from wizard import Wizard


class Ward(pygame.sprite.Sprite):
    '''
    class for running Ward(to make the dogde chance greater using a spell)
    '''

    def __init__(self, wiz):
        
        self.wiz = wiz
        self.image = pygame.image.load("..\\sprites\\wizard.png") #TODO change
