import pygame
import wizard

missile = "..\\sprites\\missile"


class Fireball(pygame.sprite.Sprite):
    '''
    This class handles the functions of a fireball

    '''

    def __init__(self, win, dmg, target, wizard: wizard.Wizard):

        self.dmg = dmg
        self.win = win
        self.target = target
        # (self.x, self.y) = wizard.get_position()
        self.x = 100
        self.y = 200
        self.x += 20

        # load an image and blit it
        missile_load = pygame.image.load("..\\sprites\\missile.png")

        win.blit(missile_load, (self.x, self.y))

        # call move()

    # TODO: define a move function that:
        # moves along until it hits something
        # when it does hit something, deal damage to it
        # otherwise, stop when it hits the edge
        # def move(self, win, dmg, target):
