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

# choice buttons should be deletet as soon as one of them is clicked aka process choice is called
# when going into start menu through button inae start menu the text box and everything else should not be cleared meaning that the satart game function only gets called on the first press of the start button any press after that should result in simply showing the main widnow again and not calling any other function just like
# choice buttons still dont get deleted when pressing any of them 

# NEEEEEEEEEEEEEEEEEEEEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

# coins get multiplied by 2 when adding to attributes or when displaying in stats table maybe too many iterations

# COMMENTS AND STUFF

# and add grid between the items and headers in the inventory table
