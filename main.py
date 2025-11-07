"""
Point d'entrée du jeu Cookie Clicker.
Gère l'affichage du menu et la boucle principale du jeu.
"""

import pygame
from ui.menu_views import Menu
from core.scene_manager import SceneManager

pygame.init()  # pylint: disable=no-member
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Cookie Clicker")

menu = Menu(screen)
scene_manager = SceneManager()
running = True  # pylint: disable=invalid-name

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pylint: disable=no-member
            running = False  # pylint: disable=invalid-name
        elif event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
            clicked = menu.click(event.pos)
            if clicked == "jouer":
                scene_manager.change_scene("jeu")
            elif clicked == "quitter":
                running = False  # pylint: disable=invalid-name

    # Dessiner selon la scène
    if scene_manager.get_scene() == "menu":
        menu.draw()
    elif scene_manager.get_scene() == "jeu":
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 50)
        text_surface = font.render("Jeu lancé !", True, (0, 0, 0))
        screen.blit(text_surface, (250, 400))

    pygame.display.flip()

pygame.quit()  # pylint: disable=no-member
