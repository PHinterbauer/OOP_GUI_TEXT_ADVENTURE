# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./main.py
# Main file to start the game
# ====================================

from utilities.game import Game, Player
from gui.interactions import load_settings

if __name__ == "__main__":
    load_settings()
    Game.main_character = Player(current_location="start", attributes={"Stärke": 0, "Leben": 0, "Münzen": 0}, inventory={})
    Game.json_file_path = "./resources/json/story_text.json"
    Game.start()

# Todo:
# - GUI Main Story Loop - Main Window
# - GUI Main Story Loop Choice Buttons
# - GUI Stats - Tabele in bottom left corner of main window
# - GUI Inventory

# - GUI Enter - can be used with GUI Input
# - GUI Input - Even needed? - done but not tested yet
# - GUI Pictures - Resize using precomputed pictures for diffrent sizes of teh Window

# - Comments
# - Docstrings
# - Function return values - func() -> None

# - look at save copilot chat for notes (Implementing GUI features and enhancments)
# - let copilot check code for errors and improvements - git graph button

# fix file location -> see notes
