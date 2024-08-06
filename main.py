import pygame
from game import Game

pygame.init()

# Génère la fenêtre de jeu.
pygame.display.set_caption("EcoHero: The Last Stand")
screen = pygame.display.set_mode((1080, 560))

# Definit le fond d'ecran.
background = pygame.image.load('assets/bg.jpg')

# Charger le jeu.
game = Game()

# La fenêtre reste ouverte tant que la variable est "True".
running = True

# Condition pour la gestion de la fenêtre
while running:

    # Appliquer la surface "background" sur l'ecran "screen".
    screen.blit(background, (0, 0))

    # Appliquer image joueur
    screen.blit(game.player.image, game.player.rect)

    # Verifier le deplacmeent du joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 920:
        game.player.mouve_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 10:
        game.player.mouve_left()

    # Mettre à jour l'ecran.
    pygame.display.flip()

    # On récupère l'événement effectué.
    for event in pygame.event.get():
        # Si l'événement est "fermé" alors, on quitte la page.
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()

        # Si l'evenement est lacher une touche on...
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
