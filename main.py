# ======================================
#     Flying Humpty text adventure
# ======================================

# Paul Hinterbauer
# 2024

from modules.game import Game, Player

# Basic settings
Game.json_file_path = "./modules/story_text.json"
Game.sleep_time = 0.04 # does not affect story related sleep times
Game.separator_length = 120
Game.main_character = Player(current_location = "start", attributes = {"Stärke": 0, "Leben": 0, "Münzen": 0}, inventory = {})

# Starts the game
Game.start()