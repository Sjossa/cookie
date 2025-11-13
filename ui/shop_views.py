import pygame


class ShopStyle:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.SysFont("Arial", 36)
        self.font_text = pygame.font.SysFont("Arial", 24)

    def draw_background(self):
        """Dégradé jaune → orange"""
        height = self.screen.get_height()
        for y in range(height):
            color = (255, 255 - int(y / 4), 100)
            pygame.draw.line(self.screen, color, (0, y),
                             (self.screen.get_width(), y))

    def draw_header(self):
        title = self.font_title.render("Welcome to the Shop",
                                       True, (60, 30, 10))
        self.screen.blit(
            title, (self.screen.get_width() // 2 - title.get_width() // 2, 20)
        )


class ShopViews:
    def __init__(self, screen):
        self.screen = screen
        self.font_text = pygame.font.SysFont("Arial", 24)

        self.items = [
            {
                "name": "Grand-mère",
                "img_path": "ui/assets/images/grand_mere (1).png",
                "price": 50,
            },
            {"name": "Maison", "img_path": "ui/assets/images/pixel.webp",
             "price": 200},
        ]

        # Préparation des images et positions
        spacing_y = 160
        for i, item in enumerate(self.items):
            image = pygame.image.load(item["img_path"]).convert_alpha()

            max_w, max_h = 100, 100
            image = self.scale_image_to_fit(image, max_w, max_h)

            item["img"] = image
            item["rect"] = image.get_rect(topleft=(140, 130 + i * spacing_y))

    def scale_image_to_fit(self, image, max_width, max_height):
        """Redimensionne l'image pour qu'elle tienne dans une zone donnée."""
        w, h = image.get_size()
        ratio = min(max_width / w, max_height / h)
        new_size = (int(w * ratio), int(h * ratio))
        return pygame.transform.smoothscale(image, new_size)

    def draw(self):
        """Affiche chaque carte d’objet"""
        for item in self.items:
            card_rect = pygame.Rect(100, item["rect"].y - 20, 600, 140)

            # Fond de carte
            pygame.draw.rect(self.screen, (250, 240, 210), card_rect,
                             border_radius=10)
            pygame.draw.rect(
                self.screen, (180, 150, 100), card_rect, 3, border_radius=10
            )

            img_rect = item["img"].get_rect(
                midleft=(card_rect.x + 80, card_rect.centery)
            )
            self.screen.blit(item["img"], img_rect)

            name_text = self.font_text.render(item["name"], True, (50, 30, 0))
            price_text = self.font_text.render(
                f"Prix : {item['price']}", True, (80, 50, 10)
            )

            self.screen.blit(name_text, (img_rect.right + 40,
                                         card_rect.y + 30))
            self.screen.blit(price_text, (img_rect.right + 40,
                                          card_rect.y + 75))
