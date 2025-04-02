# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./main.py
# Main file to start the game
# ====================================

# Basic settings
from modules.game.game_interactions import load_settings

GUI_MODE = True

def configure_game():
    """Configures the game with initial settings."""
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
    from modules.gui.design_interactions import open_main_window, confirm_player_name, resize_pictures, open_settings_window
    from modules.gui.design import StartWindow
    root = StartWindow(open_main_window, confirm_player_name, resize_pictures)

    # Add a button to open the settings menu
    settings_button = cTk.CTkButton(root, text="Settings", command=lambda: open_settings_window(root))
    settings_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    load_settings()  # Load settings before starting the game
    configure_game()  # Configure the game with initial settings
    if not GUI_MODE:
        from modules.game import Game
        Game.start()
    else:
        start_gui()

# Todo:
# - GUI Main Story Loop - Main Window
# - GUI Inventory
# - GUI Stats
# - GUI Enter - can be used with GUI Input
# - GUI Input - Even needed?
# - GUI Pictures - Resize using precomputed pictures for diffrent sizes of teh Window
# - GUI Main Story Loop Choice Buttons
# - Comments
# - Docstrings
# - Function return values - func() -> None

# - Maybe Settings Menu - everything in Configure Game function

# - look at save copilot chat for notes (Implementing GUI features and enhancments)