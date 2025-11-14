import pygame
import os
from ui.menu_views import Menu
from ui.GameView import Game
from ui.ShopView import ShopViews
from core.scene_manager import SceneManager
from game.GameController import ClickMenu, ClickGame, ClickShop
from core.EventManager import EventManager, BuyItem

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Cookie Clicker")

game = Game(screen)
scene_manager = SceneManager()
event_manager = EventManager(game)
menu = Menu(screen, event_manager)

controller = ClickMenu(screen, scene_manager, menu, game)
cookie_game = ClickGame(screen, scene_manager, menu, game, event_manager)

clock = pygame.time.Clock()
running = True

while running:

    dt = clock.tick(60) / 1000  # delta time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            controller.menu_event(event)
            if scene_manager.get_scene() == "jeu":
                cookie_game.cookie_event(event)

    controller.draw()

    if scene_manager.get_scene() == "jeu":
        game.update(dt)
        cookie_game.draw()
        event_manager.ClickBonus()

    pygame.display.flip()

if hasattr(event_manager, "shop_process"):
    event_manager.shop_process.terminate()
pygame.quit()
