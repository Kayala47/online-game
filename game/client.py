from typing import NewType
import pygame
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

fire_sign = pygame.image.load("..\\sprites\\fireball-sign.png")
fire_signHB = fire_sign.get_rect(topleft=(800, 100))



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

while True:

    win.blit(bg, (0,0))
    

    if (playerTurn == True):

        win.blit(fire_sign, (800, 100))
        wizard.update()
        pygame.display.update()

        if repeat == True:
            win.blit(fb.get_image(), fb.get_pos())
            repeat = fb.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if (pygame.mouse.get_pressed() == (True, False, False)):
                    
                    mousePos = pygame.mouse.get_pos()
                    
                    print(str(mousePos)+"this one")
                    print(str(fire_signHB)+"this one")
                    

                    if pygame.Rect.collidepoint(fire_signHB, mousePos):
                        
                        fb = Fireball(win, 10, wizard, wizard)
                        if fb.move() == True:
                            repeat = True
                            win.blit(fb.get_image(), fb.get_pos())
                        else:
                            repeat = False
                    if pygame.Rect.collidepoint(wizard.hitbox, mousePos):
                        if (wizard.take_damage(10) == True):
                            
                            win.blit(bg, (0, 0))

        pygame.display.update()

        playerTurn = False


    else:
        print("todo work in progress")
# while True:
#     # win.fill("white")
#     # print(number)
#     #number += 1

#     # pygame.mixer.Sound.play(wizard_blast)

#     win.blit(bg, (0, 0))
#     # win.blit(wizard, (START_X, GROUND))
#     # pygame.display.update()

#     wizard.update()
#     #print("blit working")
#     # missile.update()
#     win.blit(fire_sign, (800, 100))

#     #print("josh died")

    
#     pygame.display.update()

    
#     if repeat == True:
#         win.blit(fb.get_image(), fb.get_pos())
#         repeat = fb.move()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             pygame.quit()

#         if event.type == pygame.MOUSEBUTTONDOWN:
            
#             if (pygame.mouse.get_pressed() == (True, False, False)):
                
#                 mousePos = pygame.mouse.get_pos()
                
#                 print(str(mousePos)+"this one")
#                 print(str(fire_signHB)+"this one")


#                 # if (m_x >= wizard.hitbox and m_y >= wizard.hitbox and ):

#                 #     fireball.move()    pygame.Rect.collidepoint(fire_signHB, mousePos)
                

#                 if pygame.Rect.collidepoint(fire_signHB, mousePos):
                    
#                     fb = Fireball(win, 10, wizard, wizard)
#                     if fb.move() == True:
#                         repeat = True
#                         win.blit(fb.get_image(), fb.get_pos())
#                     else:
#                         repeat = False
#                 if pygame.Rect.collidepoint(wizard.hitbox, mousePos):
#                     if (wizard.take_damage(10) == True):
                        
#                         win.blit(bg, (0, 0))
                

# def kill():
#    print ("josh died")

# kill()
