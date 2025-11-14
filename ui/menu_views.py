import pygame
from .Button import Button
from core.SaveManager import SaveManager


class Menu:
    def __init__(self, screen, event_manager):
        self.screen = screen
        self.event_manager = event_manager
        self.button_jouer = Button("Jouer", 300, 400, 200, 50)
        self.button_new = Button("New", 300, 470, 200, 50)
        self.save_manager = SaveManager(self.event_manager)

    def draw(self):
        self.screen.fill((0, 0, 255))
        font = pygame.font.Font(None, 50)
        text_surface = font.render("Bienvenue", True, (0, 0, 0))
        text_x = (800 - text_surface.get_width()) // 2
        text_y = 200
        self.screen.blit(text_surface, (text_x, text_y))
        self.button_jouer.draw(self.screen)
        self.button_new.draw(self.screen)

    def click(self, pos):
        if self.button_jouer.is_clicked(pos):
            return "jouer"
        if self.button_new.is_clicked(pos):
            self.save_manager.ResetScore()
            return "jouer"
        return None
