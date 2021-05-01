import pygame
import wizard
import time

missile = "..\\sprites\\missile"
fire_sign = pygame.image.load("..\\sprites\\fireball-sign.png")


class Fireball(pygame.sprite.Sprite):
    '''
    This class handles the functions of a fireball

    '''

    def __init__(self, win, dmg, target, wizard: wizard.Wizard):

        pygame.sprite.Sprite.__init__(self)

        self.dmg = dmg
        self.win = win
        self.target = target
        # (self.x, self.y) = wizard.get_position()
        self.x = 170
        self.y = 223
        self.x += 20

        # load an image and blit it
        self.missile_load = pygame.image.load("..\\sprites\\missile.png")

        self.fire_sign = fire_sign

        win.blit(self.missile_load, (self.x, self.y))

        #win.blit(self.fire_sign, (400, 60))

        self.move()

    def move(self):

        width = self.win.get_width()
        # print(width)

        while self.x < width:
            self.x += 0.001

            # time.sleep(1)

            self.win.blit(self.missile_load, (self.x, self.y))

            self.win.blit(self.fire_sign, (400, 60))

        self.kill()
        # call move()

    # TODO: define a move function that:
        # moves along until it hits something
        # when it does hit something, deal damage to it
        # otherwise, stop when it hits the edge
        # def move(self, win, dmg, target):
