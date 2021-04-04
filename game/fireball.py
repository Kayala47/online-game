import pygame
import game.wizard

missile = "..\\sprites\\missile"


class Fireball(pygame.sprite.Sprite):
    '''
    This class handles the functions of a fireball

    '''

    def __init__(self, win, dmg, target, wizard):

        self.dmg = dmg
        self.win = win
        self.target = target

         
        # load an image and blit it
        missile_load = pygame.image.load("..\\sprites\\missile.png")
        win.blit(missile_load, (wizard.START_X += 50, 70))

        # call move()

    # TODO: define a move function that:
        # moves along until it hits something
        # when it does hit something, deal damage to it
        # otherwise, stop when it hits the edge
        def move(self, win, dmg, target):
