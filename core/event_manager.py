import subprocess
import pygame
import json
import os
import time

SCORE_FILE = "score.json"


class EventManager:
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.items_owned = 0
        self.load_score()
        self.boutique_opened = False

    def load_score(self):
        if os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, "r") as f:
                data = json.load(f)
                self.score = data.get("score", 0)
                self.items_owned = data.get("items_owned", 0)

    def save_score(self):
        with open(SCORE_FILE, "w") as f:
            json.dump({"score": self.score, "items_owned": self.items_owned}, f)

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
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def execute(self, cost=10):
        self.event_manager.load_score()

        if self.event_manager.items_owned > 1:
            cost = 20



        if self.event_manager.score >= cost:
            self.event_manager.score -= cost
            self.event_manager.items_owned += 1
            self.event_manager.save_score()
            bonus = BonusItem(self.event_manager)
            bonus.ClickBonus()

            print(
                f"Achat réussi ! Items: {self.event_manager.items_owned}, Score restant: {self.event_manager.score}"
            )

        else:
            print("Pas assez de score")


class BonusItem:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.last_update = time.time()

    def ClickBonus(self):
        now = time.time()
        if now - self.last_update >= 0:
            if self.event_manager.items_owned > 0:
                self.event_manager.load_score()
                self.event_manager.score += self.event_manager.items_owned
                self.event_manager.save_score()
                self.last_update = now
