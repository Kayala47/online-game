import pygame
#this imports the libary pygmae


# wizard = pygame.image.load("..\\sprites\\wizard.png")
START_X = 100
END_x = 470
GROUND = 200
#set varible that are used to find where wizard should be.


class Wizard(pygame.sprite.Sprite):
    '''
    This class is responsible for generation of the wizard sprite, and its sounds and associated sprites
    Inputs:
    pygame.sprite.Sprite - imports pygame Sprite functions

    '''

    def __init__(self, place: str, sound_set: float = 0.1):
        '''
        Description:
        Init is initalizing  these varibles to set things that the client.py is using to use in fuctions below
        Input:
        place is the part where the wizard might show up. Possible inputs are "left" or "right"
        sound_set is used to tell what volume level the user wants. the sound levels can be set to 0.0 - 1. Defaults to 0.1, which Josh says is already too loud
        '''

        # super().__init__()

        # this does blah blah
        wizard_blast.set_volume(sound_set)
        #this mkae it so they cna change the volume

        if (place == "left"):
            win.blit(wizard, (START_X, GROUND))

        else:
            win.blit(wizard, (END_X, GROUND))

        #the if and else means if it calls left go left but if not then right

        pygame.mixer.Sound.play(wizard_blast)

        pygame.display.update()
        #to update the display


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

'''
This is actually a free floating string. But the computer doesn't do anything with it.


'''
