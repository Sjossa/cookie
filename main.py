import pygame
import os
from ui.menu_views import Menu
from ui.game_view import Game
from ui.shop_views import  ShopViews
from core.scene_manager import SceneManager
from game.game_controller import ClickMenu, ClickGame, ClickShop
from core.event_manager import EventManager,BonusItem
SCORE_FILE = "score.json"


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Cookie Clicker")

menu = Menu(screen)
game = Game(screen)
scene_manager = SceneManager()
event_manager = EventManager(game)
bonus_item = BonusItem(event_manager)

controller = ClickMenu(screen, scene_manager, menu, game)
cookie_game = ClickGame(screen, scene_manager, menu, game, event_manager)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            controller.menu_event(event)
            if scene_manager.get_scene() == "jeu":
                cookie_game.cookie_event(event)

    controller.draw()
    if scene_manager.get_scene() == "jeu":
        cookie_game.draw()
        bonus_item.ClickBonus()
    pygame.display.flip()

pygame.quit()
