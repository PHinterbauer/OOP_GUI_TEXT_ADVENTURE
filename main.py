# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./main.py
# Main file to start the game
# ====================================

from modules.game import Game, Player
from modules.gui.interactions import open_main_window, confirm_player_name
from modules.gui.design import StartWindow

# Basic settings
Game.json_file_path = "./modules/story_text.json"
Game.sleep_time = 0.04 # does not affect story related sleep times
Game.separator_length = 120
Game.main_character = Player(current_location = "start", attributes = {"Stärke": 0, "Leben": 0, "Münzen": 0}, inventory = {})

def start_gui():
    root = StartWindow(open_main_window, confirm_player_name)
    root.mainloop()

flag = True
while flag:
    game_mode = input("Enter 'gui' for GUI mode or 'cmd' for Terminal mode: ")
    if game_mode.lower() in ["gui", "cmd"]:
        flag = False
        if game_mode.lower() == "cmd":
            Game.start()
        else:
            start_gui()
    else:
        print("Invalid input! [gui/cmd]")
