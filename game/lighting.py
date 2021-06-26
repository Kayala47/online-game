import pygame
from wizard import Wizard







class LightingHead(pygame.sprite.Sprite):

    
    def __init__ (self, wiz):
        self.wiz = wiz
        
        self.image = pygame.image.load("..\\sprites\\lighting90.png")

class LightingTail(pygame.sprite.Sprite):

    
    def __init__(self, wiz):
        self.wiz = wiz

        self.image = pygame.image.load("..\\sprites\\lighting90.png")