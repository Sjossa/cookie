import pygame

class Shop_Views:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("ui/assets/images/grand_mere (1).png").convert_alpha()

        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect(topleft=(0, 0))

    def draw(self):
        self.screen.blit(self.image, (0, 0))

        
