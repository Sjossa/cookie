# shop_views.py
import pygame


class ShopViews:
    def __init__(self, screen):
        self.screen = screen
        self.font_text = pygame.font.SysFont("Arial", 24)

        # Items classiques
        self.items = [
            {
                "name": "Grand-mère",
                "img_path": "ui/assets/images/grand_mere (1).png",
                "price": 10,
                "id": 1,
            },
            {
                "name": "Maison",
                "img_path": "ui/assets/images/pixel.webp",
                "price": 50,
                "id": 2,
            },
            {
                "name": "Usine",
                "img_path": "ui/assets/images/usine.png",
                "price": 200,
                "id": 3,
            },
        ]

        # Power-ups
        self.power_ups = [
            {
                "name": "Double Click",
                "img_path": "ui/assets/images/double_click.webp",
                "price": 1000,
                "id": 101,
            },
            {
                "name": "Auto Clicker",
                "img_path": "ui/assets/images/Mega.webp",
                "price": 1000,
                "id": 102,
            },
            {
                "name": "Mega Click",
                "img_path": "ui/assets/images/Mega.webp",
                "price": 700,
                "id": 103,
            },
        ]

        # Préparer les images
        self.prepare_images(self.items)
        self.prepare_images(self.power_ups)

    def prepare_images(self, items):
        for item in items:
            img = pygame.image.load(item["img_path"]).convert_alpha()
            w, h = img.get_size()
            ratio = min(100 / w, 100 / h)
            item["img"] = pygame.transform.smoothscale(
                img, (int(w * ratio), int(h * ratio))
            )
            item["rect"] = item["img"].get_rect()  # x,y sera défini plus tard

    def draw_card(self, item, x, y, width=250):
        card_rect = pygame.Rect(x, y - 20, width, 140)
        # Fond
        pygame.draw.rect(self.screen, (250, 240, 210), card_rect, border_radius=10)
        pygame.draw.rect(self.screen, (180, 150, 100), card_rect, 3, border_radius=10)

        # Image
        img_rect = item["img"].get_rect(midleft=(card_rect.x + 60, card_rect.centery))
        self.screen.blit(item["img"], img_rect)

        # Texte
        name_surf = self.font_text.render(item["name"], True, (50, 30, 0))
        price_surf = self.font_text.render(
            f"Prix : {item['price']}", True, (80, 50, 10)
        )
        self.screen.blit(name_surf, (img_rect.right + 20, card_rect.y + 30))
        self.screen.blit(price_surf, (img_rect.right + 20, card_rect.y + 75))

        # Met à jour le rect pour la détection des clics
        item["rect"].x = card_rect.x
        item["rect"].y = card_rect.y
        item["rect"].width = card_rect.width
        item["rect"].height = card_rect.height

    def draw(self):
        spacing_y = 160
        for i, item in enumerate(self.items):
            self.draw_card(item, 100, 130 + i * spacing_y)
        for i, item in enumerate(self.power_ups):
            self.draw_card(item, 400, 130 + i * spacing_y)
