import pygame


class game:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        self.screen.fill((0, 0, 255))
        image = pygame.image.load("./assets/images/image.png").convert_alpha

    runnig = True

    while continuer:
    ecran.blit(image, (0, 50))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False
    pygame.display.flip()
