import subprocess
import pygame
import json
import os
import time

SCORE_FILE = "data/score.json"


class EventManager:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.Grany = 0
        self.house = 0
        self.load_score()
        self.boutique_opened = False

    def load_score(self):
        if os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, "r") as f:
                data = json.load(f)
                self.score = data.get("score", 0)
                self.Grany = data.get("Grany", 0)
                self.house = data.get("house", 0)

    def save_score(self):
        with open(SCORE_FILE, "w") as f:
            json.dump(
                {"score": self.score, "Grany": self.Grany, "house": self.house}, f
            )

    def handle_click(self, event):

        self.load_score()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.game.rect.collidepoint(event.pos):
                self.score += 1
                self.save_score()

            if self.score >= 10 and not self.boutique_opened:
                subprocess.Popen(["python3", "ui/boutique.py"])
                self.boutique_opened = True


class BuyItem:
    def __init__(self, event_manager, items_id=None):
        self.event_manager = event_manager
        self.items_id = items_id

        self.items = {
            1: {"attr": "Grany", "extra_cost": 10},
            2: {"attr": "house", "extra_cost": 20},
        }

    def execute(self, cost=None, items_id=None):

        self.event_manager.load_score()

        if items_id not in self.items:
            print("Objet inconnu.")
            return

        item_data = self.items[items_id]
        attr = item_data["attr"]
        extra_cost = item_data["extra_cost"]

        current_count = getattr(self.event_manager, attr)

        cost = cost + extra_cost * current_count

        if self.event_manager.score >= cost:
            setattr(self.event_manager, attr, current_count + 1)
            self.event_manager.score -= cost
            self.event_manager.save_score()

            print(f"{attr} acheté pour {cost} points !")

            bonus = BonusItem(self.event_manager)
            bonus.ClickBonus()
        else:
            print(f"Pas assez de score, il faut {cost} points.")


class BonusItem:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.last_update = time.time()

    def ClickBonus(self):
        now = time.time()
        if now - self.last_update >= 1:
            if self.event_manager.Grany > 0:
                self.event_manager.load_score()
                self.event_manager.score += self.event_manager.Grany
                self.event_manager.save_score()
                self.last_update = now
            if self.event_manager.house > 0:
                self.event_manager.load_score()
                self.event_manager.score += self.event_manager.house * 5
                self.event_manager.save_score()
                self.last_update = now
