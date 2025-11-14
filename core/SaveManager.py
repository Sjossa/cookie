# sauvegarde
import json
import os


class SaveManager:
    SCORE_FILE = "data/score.json"

    def __init__(self, event_manager):
        self.event_manager = event_manager

    def LoadScore(self):
        try:
            if (
                not os.path.exists(self.SCORE_FILE)
                or os.path.getsize(self.SCORE_FILE) == 0
            ):
                raise FileNotFoundError

            with open(self.SCORE_FILE, "r") as f:
                data = json.load(f)

            self.event_manager.score = data.get("score", 0)
            self.event_manager.Grany = data.get("Grany", 0)
            self.event_manager.house = data.get("house", 0)
            self.event_manager.usines = data.get("usines", 0)
            self.event_manager.auto_clicker = data.get("auto_clicker", 0)

        except (FileNotFoundError, json.JSONDecodeError):
            self.event_manager.score = 0
            self.event_manager.Grany = 0
            self.event_manager.house = 0
            self.event_manager.usines = 0
            self.event_manager.auto_clicker = 0
            self.SaveScore()

    def SaveScore(self):
        os.makedirs(os.path.dirname(self.SCORE_FILE), exist_ok=True)


        with open("data/score.json", "w") as f:
            json.dump(
                {
                    "score": self.event_manager.score,
                    "Grany": self.event_manager.Grany,
                    "house": self.event_manager.house,
                    "usines": self.event_manager.usines,
                },
                f,
                indent=4,
            )

        with open("data/powerups.json", "w") as f:
            json.dump({"auto_clicker": self.event_manager.auto_clicker}, f, indent=4)

    def ResetScore(self):
        self.event_manager.score = 0
        self.event_manager.Grany = 0
        self.event_manager.house = 0
        self.event_manager.usines = 0
        self.event_manager.auto_clicker = 0
        self.SaveScore()
