import pygame
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.ShopView import ShopViews
from game.GameController import ClickShop
from core.EventManager import EventManager
from ui.GameView import Game

# Initialisation Pygame
pygame.init()
os.environ["SDL_VIDEO_WINDOW_POS"] = "820,0"

screen_shop = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Boutique")

# Création des instances
shop = ShopViews(screen_shop)
game_instance = Game(screen_shop)
event_manager = EventManager(game_instance)
click_shop_instance = ClickShop(shop, event_manager)

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
