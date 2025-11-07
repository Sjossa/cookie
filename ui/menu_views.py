import pygame
from .button import Button


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.button_jouer = Button("Jouer", 300, 400, 200, 50)
        self.button_new = Button("New", 300, 470, 200, 50)

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
        return None
