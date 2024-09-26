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

    #recuperer les projectiles du joueur
    for projectile in game.player.all_projectile:
        projectile.move()

    #appliquer les images de mon groupe de projectiles
    game.player.all_projectile.draw(screen)

    # Verifier le deplacmeent du joueur
    if game.pressed.get(pygame.K_LEFT) and game.pressed.get(pygame.K_RIGHT):
        game.player.stop()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 15:
        game.player.mouve_left()
    elif game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + (game.player.rect.width + 15) < screen.get_width():
        game.player.mouve_right()

    # Mettre à jour l'ecran.
    pygame.display.flip()

    # On récupère l'événement effectué.
    for event in pygame.event.get():
        # Si l'événement est "fermé" alors, on quitte la page.
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Si l'evenement est de tenir ou lacher une touche on...
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter que la touche espace est enclenchée
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
