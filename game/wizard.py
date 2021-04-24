import pygame
import random
# this imports the libary pygmae
#import fireball

START_X = 100

END_X = 470
GROUND = 200
# set varible that are used to find where wizard should be.


class Wizard(pygame.sprite.Sprite):
    '''
    This class is responsible for generation of the wizard sprite, and its sounds and associated sprites
    Inputs:
    pygame.sprite.Sprite - imports pygame Sprite functions

    '''

    # stats:

    # how much health the wizard has
    START_HEALTH = 10

    BASE_DAMAGE = 4  # how much damage its main attack does

    # SPEED = 20

    BASE_DODGE_CHANCE = 1  # /100, probability of dodging an attack

    LEVEL_CAP = 49

    def __init__(self, win: pygame.Surface, place: str = "left", sound_set: float = 0.1):
        '''
        Description:
        Init is initalizing  these varibles to set things that the client.py is using to use in fuctions below
        Input:
        place is the part where the wizard might show up. Possible inputs are "left" or "right"
        sound_set is used to tell what volume level the user wants. the sound levels can be set to 0.0 - 1. Defaults to 0.1, which Josh says is already too loud
        '''

        # super().__init__()
        # set all stats
        self.lvl = 1
        self.hp = self.START_HEALTH * self.lvl
        self.damage = self.BASE_DAMAGE + (1 * self.lvl)
        self.dodge_chance = self.BASE_DODGE_CHANCE + (2 * self.lvl)
        self.win = win

        self.x = START_X
        self.y = GROUND

        # TODO: define hitbox for the wizard
        self.dodge()

        # loading an image josh drew
        self.wizard_img = pygame.image.load("..\\sprites\\wizard.png")

        # loading a sound we found online for the wizard's magic blast
        wizard_blast = pygame.mixer.Sound("..\\sounds\\alien_blast.wav")

        # this mkae it so they cna change the volume
        wizard_blast.set_volume(sound_set)

        # the if and else means if it calls left go left but if not then right
        if (place == "left"):
            win.blit(self.wizard_img, (START_X, GROUND))

        else:
            win.blit(self.wizard_img, (END_X, GROUND))

        pygame.mixer.Sound.play(wizard_blast)

        pygame.display.update()
        # to update the display

    def get_position(self):
        return (self.x, self.y)

    def get_current_health(self):
        return self.health

    def get_max_health(self):
        return self.START_HEALTH * self.lvl

    def take_damage(self, amt: int):
        self.health -= amt

    def heal(self, amt: int):
        # the wizard can only be healed to a certain amount. We make sure his health doesn't go above that
        self.health = min(self.health + amt, self.get_max_health())

    # TODO: define functions to set dodge chance, increase it - JOSH HW
    def random_dodge(self):
        random_chance = random.randint(0, 100)
        return random_chance

    def dodge(self):
        random_number = self.random_dodge()

        print(random_number)

    # a function to level up - increase all his stats.
    def level_up(self):
        self.lvl += 1
        self.hp = self.START_HEALTH * lvl
        self.damage = self.BASE_DAMAGE + (1 * lvl)
        self.dodge_chance = self.BASE_DODGE_CHANCE + (2 * lvl)

    # TODO: define a funciton to launch a magic blast
    def update(self):
        self.win.blit(self.wizard_img, (self.x, self.y))

        # define a new class for the fireball

        # TODO: define a function to move the wizard

        # TODO: define a funciton to launch the magic nuke


def test():
    # this is supposed to be a comment, but is not an unconnected string
    "hello"
    # '''
    # This function exitss entirely to mess with Josh
    # Inputs:
    # none
    # '''
    print("hi!")


print(test.__doc__)
# this is too print the doc of test wihc is the first commment

win = pygame.display.set_mode((100, 100))
print(type(win))


'''
This is actually a free floating string. But the computer doesn't do anything with it.


'''

test()
