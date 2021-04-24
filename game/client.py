import pygame
#import network
import pickle
from wizard import Wizard
import fireball

pygame.font.init()

pygame.init()
pygame.mixer.init()


width = 600
height: int = 289

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Is_this_working")

bg = pygame.image.load("..\\sprites\\backround.png")
# wizard = pygame.image.load("..\\sprites\\wizard.png")
wizard = Wizard(win)


# comment every single line like this
# after comments work too

number = 0
GROUND = 200
START_X = 100

phrase = "hahaha josh lost his code :P"

while True:
    # win.fill("white")
    # print(number)
    #number += 1

    # pygame.mixer.Sound.play(wizard_blast)

    win.blit(bg, (0, 0))
    # win.blit(wizard, (START_X, GROUND))
    # pygame.display.update()

    fb = fireball.Fireball(win, 10, wizard, wizard)
    wizard.update()
    #missile.update()

    

    #print("josh died")

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("is it working")
            if (pygame.mouse.get_pressed() == (True, False, False)):
                if (wizard.take_damage(10) == True):
                    print("blit")
                    win.blit(bg, (0, 0))
                print("hello")

# def kill():
#    print ("josh died")

# kill()
