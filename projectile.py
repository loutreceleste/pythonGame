import pygame


#definir la classe du projectile
class Projectile(pygame.sprite.Sprite):

    #definiition du constructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 50

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
        self.rect.x += self.velocity

        #verifier que le projectile est parti de l'ecran
        if self.rect.x > 1080:
           self.remove()
