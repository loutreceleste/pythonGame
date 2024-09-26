import pygame
from projectile import Projectile

# Creation d'une class pour le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 4
        self.all_projectile = pygame.sprite.Group()
        self.image_right = pygame.image.load('assets/arbre_droite.png')
        self.image_left = pygame.image.load('assets/arbre_gauche.png')
        self.image = self.image_right
        self.rect = self.image_right.get_rect()
        self.rect.x = 460
        self.rect.y = 340

    def launch_projectile(self):
        if self.image == self.image_right:
            self.all_projectile.add(Projectile(self))

    def mouve_right(self):
        self.rect.x += self.velocity
        self.image = self.image_right
        self.velocity = 1

    def mouve_left(self):
        self.rect.x -= self.velocity
        self.image = self.image_left
        self.velocity = 1

    def stop(self):
        self.velocity = 0
