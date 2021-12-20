import pygame as pygame
import random


pygame.font.init()

pygame.init()
pygame.mixer.init()

width: int = 1200
height: int = 630
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Is_this_working")

bg = pygame.image.load("..\\sprites\\\\better-background.png")

all_sprites = pygame.sprite.Group()


targetList = []

backgroundWidth = bg.get_width()
number = 0
GROUND = 200
START_X = 100

run = True
class Bullet(pygame.sprite.Sprite):
     def __init__(self, speed, image):
        super().__init__()
        self.pos = pygame.Vector2(0, 0)
        self.set_target((0, 0))
        self.image = pygame.image.load("..\\sprites\\missile.png")
        self.rect = self.image.get_rect()
        speed = speed
     def set_target(self, pos):
        self.target = pygame.Vector2(pos)

     def update(self):
        move = self.target - self.pos
        move_length = move.length()

        if move_length < self.speed:
            self.pos = self.target
        elif move_length != 0:
            move.normalize_ip()
            move = move * self.speed
            self.pos += move

        self.rect.topleft = list(int(v) for v in self.pos)

while run:

    

    win.blit(bg, (0,0))
    all_sprites.update()
    #all_sprites.draw(win)
    round = 0
    group = pygame.sprite.Group(
    Bullet(1.5, pygame.Color('white')))



    
    # if repeat == True:
    # #TODO stop flickering
    #     win.blit(fb.get_image(), fb.get_pos())
    
    #     repeat = fb.move()
    while not quit:
        for event in pygame.event.get():

            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pressed() == (True, False, False)):
                
                    for Bullet in group.sprites():
                        Bullet.set_target(pygame.mouse.get_pos())
                        print("it is wokring")

                group.update()
                    
            # if (pygame.mouse.get_pressed() == (True, False, False)):
                
            #     mousePos = pygame.mouse.get_pos()
                
                # print(str(mousePos)+"this one")
                # print(str(fire_signHB)+"this one")
                # print(str(lightning_signHB)+"maybe this one")
                

                
                        

              
                    

             
        
    
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    pygame.display.flip()

