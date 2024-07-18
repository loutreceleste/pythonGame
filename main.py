import pygame
pygame.init()

# Génère la fenêtre de jeu.
pygame.display.set_caption("EcoHero: The Last Stand")
pygame.display.set_mode((700, 500))

# La fenêtre reste ouverte tant que la variable est "True"
running = True

# Condition pour la gestion de la fenêtre
while running:

    # On récupère l'événement effectué.
    for event in pygame.event.get():
        # Si l'événement est "fermé" alors, on quitte la page.
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()