import time
import subprocess
import pygame
from core.SaveManager import SaveManager


class EventManager:
    def __init__(self, game):
        self.game = game
        self.score = 0

        # Quantités des bâtiments
        self.Grany = 0
        self.house = 0
        self.usines = 0

        # Autres améliorations
        self.double_click = 0
        self.mega_click = 0

        self.boutique_opened = False
        self.save = SaveManager(self)

        self.last_update = 0.0

    def handle_click(self, event):
        """Gère le clic sur le cookie + ouverture boutique."""
        self.save.LoadScore()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.game.rect.collidepoint(event.pos):
                bonus = 1
                if getattr(self, "double_click", 0) > 0:
                    bonus *= 2
                if getattr(self, "mega_click", 0) > 0:
                    bonus *= 1
                self.score += bonus
                self.save.SaveScore()

            if self.score >= 10 and not self.boutique_opened:
                subprocess.Popen(["python3", "ui/Shop.py"])
                self.boutique_opened = True
                if hasattr(self, "shop_process"):
                    self.shop_process.terminate()

    def ClickBonus(self):
        """Ajoute les revenus passifs une fois par seconde."""
        now = time.time()

        if now - self.last_update < 1:
            return

        buildings = {
            "Grany": (1, self.Grany),
            "house": (10, self.house),
            "usines": (500, self.usines),
        }

        for name, (value, quantity) in buildings.items():
            if quantity > 0:
                self.save.LoadScore()
                self.score += value * quantity
                self.save.SaveScore()

        self.last_update = now


class BuyItem:
    def __init__(self, event_manager, items_id=None):
        self.event_manager = event_manager
        self.items_id = items_id

        self.items = {
            1: {"attr": "Grany", "extra_cost": 10 * (1.15**self.event_manager.Grany)},
            2: {"attr": "house", "extra_cost": 20 * (1.15**self.event_manager.house)},
            3: {"attr": "usines", "extra_cost": 50 * (1.15**self.event_manager.usines)},
        }

        self.item2 = {
            101: {"attr": "double_click", "extra_cost": 1000},
            # 102: {"attr": "auto_clicker", "extra_cost": 1500},
            103: {"attr": "mega_click", "extra_cost": 700},
        }

    def execute(self, cost=0, items_id=None):
        """Achète un objet de la boutique, que ce soit bâtiment ou power-up."""
        self.event_manager.save.LoadScore()

        item_data = self.items.get(items_id) or self.item2.get(items_id)
        if not item_data:
            print("Objet inconnu.")
            return

        attr = item_data["attr"]
        extra_cost = item_data["extra_cost"]

        current_count = getattr(self.event_manager, attr, 0)
        total_cost = cost + extra_cost * current_count

        if self.event_manager.score >= total_cost:
            setattr(self.event_manager, attr, current_count + 1)
            self.event_manager.score -= total_cost
            self.event_manager.save.SaveScore()
            print(f"{attr} acheté pour {total_cost} points !")
        else:
            print(f"Pas assez de score, il faut {total_cost} points.")
