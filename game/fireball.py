import pygame
import wizard
import time

missile = "..\\sprites\\missile"


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

        self.sound_set = 0.1

        # load an image and blit it
        self.missile_load = pygame.image.load("..\\sprites\\missile.png")

        # self.fire_sign = fire_sign

        self.win.blit(self.missile_load, (self.x, self.y))

        # loading a sound we found online for the wizard's magic blast
        self.wizard_blast = pygame.mixer.Sound("..\\sounds\\alien_blast.wav")

        # this mkae it so they cna change the volume
        self.wizard_blast.set_volume(self.sound_set)

        pygame.mixer.Sound.play(self.wizard_blast)

        self.move()


    def get_image(self):
        return self.missile_load

    def get_pos(self):
        return (self.x, self.y)

    def move(self):

        width = self.win.get_width()
        # print(width


        if self.x < width:
            self.x += 0.7


            # time.sleep(1)

            self.win.blit(self.missile_load, (self.x, self.y))

            return True

        

            print(self.x)
            print(width)

        else:
            self.kill()
            return False
        
        # call move()

    # TODO: define a move function that:
        # moves along until it hits something
        # when it does hit something, deal damage to it
        # otherwise, stop when it hits the edge
        # def move(self, win, dmg, target):
