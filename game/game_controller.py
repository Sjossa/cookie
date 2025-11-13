import pygame
from core.event_manager import EventManager, BuyItem


class GameController:
    def __init__(self, screen, scene_manager, menu, game):
        self.screen = screen
        self.scene_manager = scene_manager
        self.menu = menu
        self.game = game

    def draw(self):
        current_scene = self.scene_manager.get_scene()
        if current_scene == "menu":
            self.menu.draw()
        elif current_scene == "jeu":
            self.game.draw()


class ClickMenu(GameController):
    def menu_event(self, event):
        if self.scene_manager.get_scene() == "menu":
            clicked = self.menu.click(event.pos)
            if clicked == "jouer":
                self.scene_manager.change_scene("jeu")
        return True


class ClickGame(GameController):
    def __init__(self, screen, scene_manager, menu, game, event_manager):
        super().__init__(screen, scene_manager, menu, game)
        self.event_manager = event_manager

    def draw(self):
        if self.scene_manager.get_scene() == "jeu":
            self.game.draw(self.event_manager.score)

    def cookie_event(self, event):
        self.event_manager.handle_click(event)


class ClickShop:
    def __init__(self, shop, event_manager):
        self.shop = shop
        self.event_manager = event_manager

    def shop_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, item in enumerate(self.shop.items, start=1):
                if item["rect"].collidepoint(event.pos):
                    cost = item.get("price", 10)

                    BuyItem(self.event_manager).execute(cost=cost, items_id=i)
