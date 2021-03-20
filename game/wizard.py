import pygame


wizard = pygame.image.load("..\\sprites\\wizard.png")
START_X = 100
END_x = 470
GROUND = 200

class Wizard(pygame.sprite.Sprite):


    def __init__(self, place, sound_set):

        super().__init__()

        wizard_blast.set_volume(sound_set)

        if (place == "left"):
            win.blit(wizard, (START_X, GROUND))

        else:
            win.blit(wizard, (END_X, GROUND))
        
        pygame.mixer.Sound.play(wizard_blast)

        pygame.display.update()
        






