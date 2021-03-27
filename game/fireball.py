import pygame
import game.wizard


class Fireball(pygame.sprite.Sprite):
    '''
    This class handles the functions of a fireball

    '''

    def __init__(self, win, dmg):

        self.dmg = dmg
        self.win = win

        # load an image and blit it

        # call move()

    # TODO: define a move function that:
        # moves along until it hits something
        # when it does hit something, deal damage to it
        # otherwise, stop when it hits the edge
