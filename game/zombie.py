import pygame




class Zombie(pygame.sprite.Sprite):


    '''
    class for running zombie as an enemy.
    '''

    HEALTH = 5

    DAMAGE = 3

    def __init__(self, win, x, y,  *groups):
        super().__init__(*groups)

 
        self.hp = self.HEALTH
        self.damage = self.DAMAGE
        self.x = x
        self.y = y
        self.win = win
        self.died = False
        self.zombie = pygame.image.load("..\\sprites\\zombie.png")
        self.rect = self.zombie.get_rect(topleft=(self.x, self.y))

        self.win.blit(self.zombie,(self.x, self.y))

    def getrect(self):
        return self.rect

    def update(self):
        self.rect = self.zombie.get_rect(topleft=(self.x, self.y))
        if (self.died == False):
            self.x -= 0.02
            self.win.blit(self.zombie, (self.x, self.y))

    def take_damage(self, dmg):
        print("took damage")
        self.hp -= dmg
        #print("hit")
        if self.hp <= 0:
            self.kill()
            self.died = True
        
        