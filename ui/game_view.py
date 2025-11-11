import pygame


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.image = pygame.image.load("ui/assets/images/image.png").convert_alpha()

        self.image = pygame.transform.scale_by(self.image, 0.5)

        self.rect = self.image.get_rect(topleft=(0, 0))

    def draw(self, score=0):
        self.screen.blit(self.image, (0, 0))
        score_text = self.font.render(f"Score : {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))



