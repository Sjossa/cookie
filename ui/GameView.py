import pygame
import math


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

        self.image = pygame.image.load("ui/assets/images/cookie.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.image, (200, 200))

        self.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)

        self.bouncing = False
        self.bounce_timer = 0
        self.angle = 0

        self.image_to_draw = self.original_image
        self.rect = self.image_to_draw.get_rect(center=self.center)

    def draw_background(self):
        height = self.screen.get_height()
        for y in range(height):
            color = (50, 150, 255 - int(y / 5))
            pygame.draw.line(self.screen, color, (0, y), (self.screen.get_width(), y))

    def draw(self, score=0):
        self.draw_background()
        self.screen.blit(self.image_to_draw, self.rect)
        score_text = self.font.render(f"Score : {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def click_cookie(self):
        self.bouncing = True
        self.bounce_timer = 0

    def update(self, dt):

        scale_factor = 1
        if self.bouncing:
            self.bounce_timer += dt
            scale_factor = 1 + 0.1 * (1 - abs((self.bounce_timer - 0.2) / 0.2))
            if self.bounce_timer > 0.4:
                self.bouncing = False

        # Rotation légère permanente
        self.angle += 50 * dt
        rotated = pygame.transform.rotozoom(
            self.original_image, math.sin(self.angle / 10) * 5, scale_factor
        )
        self.image_to_draw = rotated
        self.rect = self.image_to_draw.get_rect(center=self.center)
