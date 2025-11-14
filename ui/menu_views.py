import pygame
from .Button import Button
import webbrowser
from core.SaveManager import SaveManager


class Menu:
    def __init__(self, screen, event_manager):
        self.screen = screen
        self.event_manager = event_manager

        self.button_jouer = Button("Jouer", 300, 350, 200, 50)
        self.button_new = Button("Nouvelle Partie", 300, 420, 200, 50)
        self.button_exit = Button("Quitter", 300, 490, 200, 50)
        self.button_credits = Button("Crédits", 300, 560, 200, 50)

        self.save_manager = SaveManager(self.event_manager)

    def draw_background(self):
        """Dégradé vertical bleu → bleu clair."""
        h = self.screen.get_height()
        for i in range(h):
            ratio = i / h
            r = int(0 + ratio * 50)
            g = int(50 + ratio * 100)
            b = int(150 + ratio * 105)
            pygame.draw.line(self.screen, (r, g, b), (0, i), (800, i))

    def draw(self):
        self.draw_background()

        # Titre
        font = pygame.font.Font(None, 80)
        title = font.render("Bienvenue", True, (255, 255, 255))

        # Ombre légère
        shadow = font.render("Bienvenue", True, (0, 0, 0))
        self.screen.blit(shadow, (251, 101))
        self.screen.blit(title, (250, 100))

        # Boutons
        self.button_jouer.draw(self.screen)
        self.button_new.draw(self.screen)
        self.button_exit.draw(self.screen)
        self.button_credits.draw(self.screen)

    def click(self, pos):
        if self.button_jouer.is_clicked(pos):
            return "jouer"
        if self.button_new.is_clicked(pos):
            self.save_manager.ResetScore()
            return "jouer"
        if self.button_exit.is_clicked(pos):
            pygame.quit()
        if self.button_credits.is_clicked(pos):
            webbrowser.open("https://youtu.be/dQw4w9WgXcQ?si=ovwZ9ntMzQ5-9Xg8")
        return None
