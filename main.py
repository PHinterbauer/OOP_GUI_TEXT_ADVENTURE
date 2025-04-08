# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./main.py
# Main file to start the game
# ====================================

from utilities.game import Game, Player
from gui.interactions import load_settings, resource_path

if __name__ == "__main__":
    load_settings()
    Game.main_character = Player(current_location="start", attributes={"Stärke": 0, "Leben": 0, "Münzen": 0}, inventory={})
    Game.json_file_path = resource_path("resources/json/story_text.json")
    Game.start()
