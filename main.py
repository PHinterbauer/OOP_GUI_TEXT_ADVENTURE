# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./main.py
# Main file to start the game
# ====================================

# Basic settings
GUI_MODE = True

def configure_game():
    from modules.game import Game, Player
    Game.json_file_path = "./modules/story_text.json"
    Game.sleep_time = 0.04  # does not affect story-related sleep times
    Game.separator_length = 120
    Game.main_character = Player(
        current_location="start",
        attributes={"Stärke": 0, "Leben": 0, "Münzen": 0},
        inventory={},
    )

def start_gui():
    from modules.gui.interactions import open_main_window, confirm_player_name, resize_pictures
    from modules.gui.design import StartWindow
    root = StartWindow(open_main_window, confirm_player_name, resize_pictures)
    root.mainloop()

if __name__ == "__main__":
    configure_game()  # Configure the game before starting
    if not GUI_MODE:
        from modules.game import Game
        Game.start()
    else:
        start_gui()

# Todo:
# - GUI Inventory
# - GUI Stats
# - GUI Enter - can be used with GUI Input
# - GUI Input - Even needed?
# - GUI Pictures - Resize using precomputed pictures for diffrent sizes of teh Window
# - GUI Main Story Loop Choice Buttons
# - Comments
# - Docstrings
# - Function return values - func() -> None

# - Maybe Settings Menu - Configure Game
