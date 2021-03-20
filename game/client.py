import pygame
#import network
import pickle
import wizard
pygame.font.init()

pygame.init()
pygame.mixer.init()


width = 600
height = 289
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Is_this_working")

bg = pygame.image.load("..\\sprites\\backround.png")
wizard = pygame.image.load("..\\sprites\\wizard.png")

wizard_blast = pygame.mixer.Sound("..\\sounds\\alien_blast.wav") 
wizard_blast.set_volume(0.09)
number = 0
GROUND = 200
START_X = 100

while True:
    #win.fill("white")
    #print(number)
    #number += 1
    
    
    
    pygame.mixer.Sound.play(wizard_blast)

    win.blit(bg, (0, 0))
    win.blit(wizard, (START_X, GROUND))
    pygame.display.update()

    print ("josh died")










    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
#def kill():
#    print ("josh died")

#kill()


