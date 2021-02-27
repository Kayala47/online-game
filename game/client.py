import pygame
#import network
import pickle
pygame.font.init()

width = 650
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Is_this_working")

number = 0

while True:
    win.fill("white")
    #print(number)
    #number += 1
    image = pygame.image.load("C:\\Users\\Joshua\\Desktop\\online-game\\sprites\\wizard.png")
    win.blit(image, (0, 0))
    pygame.display.update()










    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
#def kill():
#    print ("josh died")

#kill()


