import json
import os


class SaveManager:
    SCORE_FILE = "data/score.json"

    def __init__(self, event_manager):
        self.event_manager = event_manager

    def LoadScore(self):
        """Charge le score, les bâtiments et les power-ups depuis les fichiers JSON."""
        try:
            # Charger score et bâtiments
            if not os.path.exists(self.SCORE_FILE) or os.path.getsize(self.SCORE_FILE) == 0:
                raise FileNotFoundError

            with open(self.SCORE_FILE, "r") as f:
                data = json.load(f)

            self.event_manager.score = data.get("score", 0)
            self.event_manager.Grany = data.get("Grany", 0)
            self.event_manager.house = data.get("house", 0)
            self.event_manager.usines = data.get("usines", 0)

            # Charger power-ups
            power_file = "data/powerups.json"
            if os.path.exists(power_file):
                with open(power_file, "r") as f:
                    power_data = json.load(f)
                self.event_manager.auto_clicker = power_data.get("auto_clicker", 0)
                self.event_manager.double_click = power_data.get("double_click", 0)
                self.event_manager.mega_click = power_data.get("mega_click", 0)
            else:
                self.event_manager.auto_clicker = 0
                self.event_manager.double_click = 0
                self.event_manager.mega_click = 0

        except (FileNotFoundError, json.JSONDecodeError):
            # Initialisation si fichiers manquants ou corrompus
            self.ResetScore()

    def SaveScore(self):
        """Sauvegarde le score, les bâtiments et les power-ups sans écraser les valeurs existantes."""
        os.makedirs(os.path.dirname(self.SCORE_FILE), exist_ok=True)

        # Sauvegarder score et bâtiments
        with open("data/score.json", "w") as f:
            json.dump({
                "score": self.event_manager.score,
                "Grany": self.event_manager.Grany,
                "house": self.event_manager.house,
                "usines": self.event_manager.usines,
            }, f, indent=4)

        # Sauvegarder power-ups sans écraser les autres
        power_file = "data/powerups.json"
        powerups = {}
        if os.path.exists(power_file):
            try:
                with open(power_file, "r") as f:
                    powerups = json.load(f)
            except json.JSONDecodeError:
                powerups = {}

        powerups.update({
            "auto_clicker": self.event_manager.auto_clicker,
            "double_click": self.event_manager.double_click,
            "mega_click": self.event_manager.mega_click,
        })

        with open(power_file, "w") as f:
            json.dump(powerups, f, indent=4)

    def ResetScore(self):
        """Réinitialise tout (score, bâtiments, power-ups) à zéro."""
        self.event_manager.score = 0
        self.event_manager.Grany = 0
        self.event_manager.house = 0
        self.event_manager.usines = 0
        self.event_manager.auto_clicker = 0
        self.event_manager.double_click = 0
        self.event_manager.mega_click = 0
        self.SaveScore()
