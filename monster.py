import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 2
        self.image = pygame.image.load('assets/centrale.png')
        self.rect = self.image.get_rect()

