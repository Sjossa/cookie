import pygame


# Classe Button
class Button:
    def __init__(
        self,
        text,
        x,
        y,
        width,
        height,
        color=(0, 200, 0),
        text_color=(0, 0, 0),
        font_size=50,
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen):

        pygame.draw.rect(screen, self.color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_x = self.rect.x + (self.rect.width - text_surface.get_width()) // 2
        text_y = self.rect.y + (self.rect.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
