from player import Player
from monster import Monster

# Creation d'une class pour le jeu
class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = {}

    def spawn_monster(self):
        monster = Monster
