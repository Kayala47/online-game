import pygame
#import network
import pickle
import wizard
import fireball

pygame.font.init()

pygame.init()
pygame.mixer.init()


width = 600
height: int = 289

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Is_this_working")

bg = pygame.image.load("..\\sprites\\backround.png")
wizard = pygame.image.load("..\\sprites\\wizard.png")

# comment every single line like this
# after comments work too

number = 0
GROUND = 200
START_X = 100

while True:
    # win.fill("white")
    # print(number)
    #number += 1

    # pygame.mixer.Sound.play(wizard_blast)

    win.blit(bg, (0, 0))
    win.blit(wizard, (START_X, GROUND))
    # pygame.display.update()

    fb = fireball.Fireball(win, 10, wizard, wizard)

    #print("josh died")

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
# def kill():
#    print ("josh died")

# kill()
