import pygame
import os
import sys



# Permet d'importer depuis la racine du projet
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shop_views import Shop_Views
from game.game_controller import ClickShop
from core.event_manager import EventManager
from game_view import Game

# Initialisation Pygame
pygame.init()
os.environ["SDL_VIDEO_WINDOW_POS"] = "820,0"  # Position de la fenêtre

screen_shop = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Boutique")

# Création des instances
shop = Shop_Views(screen_shop)
game_instance = Game(screen_shop)  # si tu veux utiliser game dans EventManager
event_manager = EventManager(game_instance)  # instanciation correcte
click_shop_instance = ClickShop(shop, event_manager)  # on passe l'instance

# Boucle principale
running_shop = True
while running_shop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_shop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_shop_instance.shop_event(event)

    screen_shop.fill((255, 255, 0))
    shop.draw()
    pygame.display.flip()

pygame.quit()


