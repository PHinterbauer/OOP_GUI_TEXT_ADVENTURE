# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./main.py
# Main file to start the game
# ====================================

# Basic settings
from modules.gui.game_interactions import load_settings
import customtkinter as cTk

def configure_game():
    from modules.game import Game, Player
    Game.gui_mode = True
    Game.json_file_path = "./modules/story_text.json"
    Game.sleep_time = 0.04  # does not affect story-related sleep times
    Game.separator_length = 120
    Game.main_character = Player(current_location="start", attributes={"Stärke": 0, "Leben": 0, "Münzen": 0}, inventory={})

def start_gui():
    from modules.gui.design_interactions import open_main_window, confirm_player_name, open_settings
    from modules.gui.design import StartWindow
    root = StartWindow(open_main_window, confirm_player_name, open_settings)
    root.mainloop()

if __name__ == "__main__":
    from modules.game import Game
    load_settings()  # Load settings before starting the game
    if not Game.gui_mode:
        Game.start()
    else:
        start_gui()

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
