import pygame



class Zombie(pygame.sprite.Sprite):


    '''
    class for running zombie as an enemy.
    '''
    def __init__(self, win, x, y,  *groups):
        super().__init__(*groups)

        self.x = self.x
        self.y = self.y
        self.zombie = pygame.image.load("..\\sprites\\zombie.png")
        self.HB = self.zombie.get_rect(topleft=(800, 200))

        self.win.blit(self.zombie,(self.x, self.y))