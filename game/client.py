from lighting import Lighting
from typing import NewType
import pygame as pygame
#import network
import pickle
from wizard import Wizard
from fireball import Fireball

pygame.font.init()

pygame.init()
pygame.mixer.init()


width: int = 1200
height: int = 630

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Is_this_working")

bg = pygame.image.load("..\\sprites\\better-background.png")

fire_sign = pygame.image.load("..\\sprites\\fire-sign.png")
fire_signHB = fire_sign.get_rect(topleft=(800, 100))

lighting_sign = pygame.image.load("..\\sprites\\lighting-sign.png")
lighting_signHB = lighting_sign.get_rect(topleft=(1000, 100))

ward_sign = pygame.image.load("..\\sprites\\ward-sign.png")
ward_signHB = ward_sign.get_rect(topleft=(800, 200))

cloud = pygame.image.load("..\\sprites\\cloud.png")

#size in pixels 177 and 78
 

# wizard = pygame.image.load("..\\sprites\\wizard.png")
wizard = Wizard(win)
#print("blit working")
# fb = Fireball(win, 10, wizard, wizard)

# comment every single line like this
# after comments work too


number = 0
GROUND = 200
START_X = 100

phrase = "hahaha josh lost his code :P"

repeat = False

playerTurn = True

conterRounds = 0

run = True

all_sprites = pygame.sprite.Group()

while run:

    


    win.blit(bg, (0,0))
    win.blit(fire_sign, (800, 100))
    win.blit(lighting_sign, (1000, 100))
    win.blit(ward_sign,(800, 200))
    win.blit(cloud, (700, 400))
    wizard.update()
    all_sprites.update()
    all_sprites.draw(win)


    
    if repeat == True:
    #TODO stop flickering
        win.blit(fb.get_image(), fb.get_pos())
    
        repeat = fb.move()

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
                    
            if (pygame.mouse.get_pressed() == (True, False, False)):
                
                mousePos = pygame.mouse.get_pos()
                
                # print(str(mousePos)+"this one")
                # print(str(fire_signHB)+"this one")
                # print(str(lighting_signHB)+"maybe this one")
                

                if pygame.Rect.collidepoint(fire_signHB, mousePos):
                    
                    fb = Fireball(win, 10, wizard, wizard)
                    if fb.move() == True:
                        repeat = True
                        win.blit(fb.get_image(), fb.get_pos())
                        fb.update()
                    else:
                        repeat = False
                        

                if pygame.Rect.collidepoint(lighting_signHB, mousePos):
                    
                    lb = Lighting(win, wizard, 800, 400, 700, 400, all_sprites)
                    lb.update()
                    

                if pygame.Rect.collidepoint(ward_signHB, mousePos):
                    
                    fb = Fireball(win, 10, wizard, wizard)
                    if fb.move() == True:
                        repeat = True
                        win.blit(fb.get_image(), fb.get_pos())
                    else:
                        repeat = False

    
    
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    pygame.display.flip()




#     #print("josh died")

    

# def kill():
#    print ("josh died")

# kill()
