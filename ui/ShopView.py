import pygame

class ShopViews:
    CARD_WIDTH = 250
    CARD_HEIGHT = 140
    CARD_BG_COLOR = (250, 240, 210)
    CARD_BORDER_COLOR = (180, 150, 100)
    NAME_COLOR = (50, 30, 0)
    PRICE_COLOR = (80, 50, 10)
    IMAGE_MAX_SIZE = 100

    def __init__(self, screen):
        self.screen = screen
        self.font_text = pygame.font.SysFont("Arial", 24)

        self.items = [
            {"name": "Grand-mère", "img_path": "ui/assets/images/grand_mere (1).png", "price": 10, "id": 1},
            {"name": "Maison", "img_path": "ui/assets/images/pixel.webp", "price": 50, "id": 2},
            {"name": "Usine", "img_path": "ui/assets/images/usine.png", "price": 200, "id": 3},
        ]

        self.power_ups = [
            {"name": "Double Click", "img_path": "ui/assets/images/double_click.webp", "price": 1000, "id": 101},
            {"name": "Auto Clicker", "img_path": "ui/assets/images/Mega.webp", "price": 1000, "id": 102},
            {"name": "Mega Click", "img_path": "ui/assets/images/Mega.webp", "price": 700, "id": 103},
        ]

        # Préparer les images
        self.prepare_images(self.items)
        self.prepare_images(self.power_ups)

    def prepare_images(self, items):
        for item in items:
            img = pygame.image.load(item["img_path"]).convert_alpha()
            w, h = img.get_size()
            ratio = min(self.IMAGE_MAX_SIZE / w, self.IMAGE_MAX_SIZE / h)
            item["img"] = pygame.transform.smoothscale(img, (int(w * ratio), int(h * ratio)))
            item["rect"] = item["img"].get_rect()

    def draw_card(self, item, x, y):
        card_rect = pygame.Rect(x, y - 20, self.CARD_WIDTH, self.CARD_HEIGHT)

        pygame.draw.rect(self.screen, self.CARD_BG_COLOR, card_rect, border_radius=10)
        pygame.draw.rect(self.screen, self.CARD_BORDER_COLOR, card_rect, 3, border_radius=10)

        img_rect = item["img"].get_rect(midleft=(card_rect.x + 60, card_rect.centery))
        self.screen.blit(item["img"], img_rect)

        self.screen.blit(self.font_text.render(item["name"], True, self.NAME_COLOR), (img_rect.right + 20, card_rect.y + 30))
        self.screen.blit(self.font_text.render(f"Prix : {item['price']}", True, self.PRICE_COLOR), (img_rect.right + 20, card_rect.y + 75))

        item["rect"].update(card_rect)

    def draw(self):
        spacing_y = 160
        for i, item in enumerate(self.items):
            self.draw_card(item, 100, 130 + i * spacing_y)
        for i, item in enumerate(self.power_ups):
            self.draw_card(item, 400, 130 + i * spacing_y)
