class SceneManager:
    def __init__(self):
        self.current_scene = "menu"

    def change_scene(self, scene_name):
        self.current_scene = scene_name
        print(f"Changement de scène → {scene_name}")

    def get_scene(self):
        return self.current_scene


class ShopManager:
    def __init__(self):
        self.shop_scene = "shop"

    def get_scene(self):
        return self.shop_scene
