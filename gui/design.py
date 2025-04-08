# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/design.py
# Design for the GUI
# ====================================

import customtkinter as cTk
from PIL import Image, ImageSequence
import json
from CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown

COLOR_SCHEMES = []

class StartWindow(cTk.CTk):
    """## StartWindow class
    Represents the main menu window of the game.
    """
    COLOR_BACKGROUND = "#2B2B2B"
    COLOR_TEXT = "#FFFFFF"
    COLOR_BUTTON = "#3C3F41"
    COLOR_BUTTON_HOVER = "#4E5254"
    COLOR_FRAME = "#3C3F41"

    def __init__(self, open_main_window, confirm_player_name, open_settings):
        """## Initializes the StartWindow
        Args:
            open_main_window (function): Callback to open the main game window.
            confirm_player_name (function): Callback to confirm the player's name.
            open_settings (function): Callback to open the settings window.
        """
        super().__init__()

        # Set up window properties
        self.player_name = ""
        self.title("The Flying Humpty - Main Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("720x320")
        self.configure(fg_color=StartWindow.COLOR_BACKGROUND)

        # Load and display pirate ship GIF
        pirate_ship_path = "./resources/gifs/PIRATE_SHIP_GIF.gif"
        self.pirate_ship_frames = [cTk.CTkImage(light_image=frame.copy(), dark_image=frame.copy(), size=(200, 200)) for frame in ImageSequence.Iterator(Image.open(pirate_ship_path))]
        self.current_frame = 0
        self.pirate_ship_label = cTk.CTkLabel(self, text="", image=self.pirate_ship_frames[self.current_frame], fg_color=StartWindow.COLOR_BACKGROUND)
        self.pirate_ship_label.place(relx=0.8, rely=0.5, anchor="center")

        self.update_gif()  # Start GIF animation

        # Load and display HWI logo
        hwi_logo_path = "./resources/images/HWI_LOGO_REMOVEDBG.png"
        self.hwi_logo_image = cTk.CTkImage(light_image=Image.open(hwi_logo_path), dark_image=Image.open(hwi_logo_path), size=(200, 200))
        self.hwi_logo_label = cTk.CTkLabel(self, text="", image=self.hwi_logo_image, fg_color=StartWindow.COLOR_BACKGROUND)
        self.hwi_logo_label.place(relx=0.2, rely=0.5, anchor="center")

        # Player name entry field
        self.player_name_entry = cTk.CTkEntry(self, placeholder_text="Enter your name", fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT)
        self.player_name_entry.place(relx=0.5, rely=0.5, anchor="center")

        # Info label for feedback
        self.info_label = cTk.CTkLabel(self, text="", fg_color=StartWindow.COLOR_BACKGROUND, text_color=StartWindow.COLOR_TEXT)
        self.info_label.place(relx=0.5, rely=0.4, anchor="center")

        # Buttons for confirming name, starting game, and opening settings
        self.confirm_player_name_btn = cTk.CTkButton(self, text="Confirm Name", command=lambda: confirm_player_name(self), fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
        self.confirm_player_name_btn.place(relx=0.5, rely=0.6, anchor="center")

        self.open_main_btn = cTk.CTkButton(self, text="Start", command=lambda: open_main_window(self), fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
        self.open_main_btn.place(relx=0.5, rely=0.7, anchor="center")

        self.open_settings_btn = cTk.CTkButton(self, text="Settings", command=lambda: open_settings(self), fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
        self.open_settings_btn.place(relx=0.5, rely=0.8, anchor="center")

    def update_gif(self):
        """## Updates the pirate ship GIF animation."""
        self.current_frame = (self.current_frame + 1) % len(self.pirate_ship_frames)
        self.pirate_ship_label.configure(image=self.pirate_ship_frames[self.current_frame])
        self.after(100, self.update_gif)  # Callback for continuous animation


class MainWindow(cTk.CTkToplevel):
    """## MainWindow class
    Represents the main game window where the story and choices are displayed.
    """
    def __init__(self, master, open_inventory, open_start_menu):
        """## Initializes the MainWindow
        Args:
            master (StartWindow): The parent StartWindow instance.
            open_inventory (function): Callback to open the inventory window.
            open_start_menu (function): Callback to return to the start menu.
        """
        super().__init__(master)

        # Set up window properties
        self.player_name = master.player_name
        self.input_callback_value = None
        self.title(f"{self.player_name}'s adventure among the Flying Humpty - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("1280x600")
        self.minsize(800, 500)
        self.configure(fg_color=StartWindow.COLOR_BACKGROUND)

        # Text box for displaying story
        self.text_box = cTk.CTkTextbox(self, fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT)
        self.text_box.place(relx=0.05, rely=0.1, relwidth=0.85, relheight=0.45)
        self.text_box.configure(state="disabled")

        # Buttons for inventory and menu
        self.open_inventory_btn = cTk.CTkButton(self, text="Inventory", command=lambda: open_inventory(self), fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
        self.open_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        self.open_menu_btn = cTk.CTkButton(self, text="Menu", command=lambda: open_start_menu(self), fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
        self.open_menu_btn.place(relx=0.0, rely=0.0, anchor="nw", x=10, y=10)

        # Frames for choices and stats
        self.choice_frame = cTk.CTkFrame(self, fg_color=StartWindow.COLOR_FRAME)
        self.choice_frame.place(relx=0.05, rely=0.68, relwidth=0.45, relheight=0.3)

        self.stats_frame = cTk.CTkFrame(self, fg_color=StartWindow.COLOR_FRAME)
        self.stats_frame.place(relx=0.51, rely=0.68, relwidth=0.39, relheight=0.3)
        self.stats_frame.grid_rowconfigure(0, weight=1)
        self.stats_frame.grid_columnconfigure(0, weight=1)

        # Frame for stats table
        self.stats_table_frame = cTk.CTkFrame(self.stats_frame, fg_color=StartWindow.COLOR_BACKGROUND)
        self.stats_table_frame.pack(fill="both", expand=True, padx=10, pady=10)


class InventoryWindow(cTk.CTkToplevel):
    """## InventoryWindow class
    Represents the inventory window where the player's items are displayed.
    """
    def __init__(self, master, close_inventory):
        """## Initializes the InventoryWindow
        Args:
            master (MainWindow): The parent MainWindow instance.
            close_inventory (function): Callback to close the inventory window.
        """
        super().__init__(master)

        # Set up window properties
        self.player_name = master.player_name
        self.title(f"{self.player_name}'s Inventory - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("800x600")
        self.configure(fg_color=StartWindow.COLOR_BACKGROUND)

        # Button to close inventory
        self.close_inventory_btn = cTk.CTkButton(self, text="Close", command=lambda: close_inventory(self), fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
        self.close_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        # Frame for inventory table
        self.inventory_table_frame = cTk.CTkFrame(self, fg_color=StartWindow.COLOR_FRAME)
        self.inventory_table_frame.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")


class SettingsWindow(cTk.CTkToplevel):
    """## SettingsWindow class
    Represents the settings window where the player can adjust game settings.
    """
    def __init__(self, master, save_and_close, set_color_scheme):
        """## Initializes the SettingsWindow
        Args:
            master (MainWindow): The parent MainWindow instance.
            save_and_close (function): Callback to save settings and close the window.
            set_color_scheme (function): Callback to set the color scheme.
        """
        super().__init__(master)

        # Set up window properties
        self.player_name = master.player_name
        self.title(f"{self.player_name}'s Settings Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("700x400")
        self.configure(fg_color=StartWindow.COLOR_BACKGROUND)

        # GUI mode switch
        self.gui_mode_label = cTk.CTkLabel(self, text="Enable GUI Mode:", fg_color=StartWindow.COLOR_BACKGROUND, text_color=StartWindow.COLOR_TEXT)
        self.gui_mode_label.place(relx=0.5, rely=0.1, anchor="center")

        self.gui_mode_switch = cTk.CTkSwitch(self, text="GUI Mode", fg_color=StartWindow.COLOR_BUTTON, progress_color=StartWindow.COLOR_BUTTON_HOVER)
        self.gui_mode_switch.place(relx=0.5, rely=0.17, anchor="center")
        self.gui_mode_switch.toggle()

        # Sleep time entry
        self.sleep_time_label = cTk.CTkLabel(self, text="Game Sleep Time (float, default=0.04):", fg_color=StartWindow.COLOR_BACKGROUND, text_color=StartWindow.COLOR_TEXT)
        self.sleep_time_label.place(relx=0.5, rely=0.3, anchor="center")

        self.sleep_time_entry = cTk.CTkEntry(self, fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT)
        self.sleep_time_entry.place(relx=0.5, rely=0.37, anchor="center")
        self.sleep_time_entry.insert(0, "0.04")

        # Separator length entry
        self.separator_length_label = cTk.CTkLabel(self, text="Separator Length (int, default=320):", fg_color=StartWindow.COLOR_BACKGROUND, text_color=StartWindow.COLOR_TEXT)
        self.separator_length_label.place(relx=0.5, rely=0.5, anchor="center")

        self.separator_length_entry = cTk.CTkEntry(self, fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT)
        self.separator_length_entry.place(relx=0.5, rely=0.57, anchor="center")
        self.separator_length_entry.insert(0, "320")

        # Color scheme dropdown
        self.color_scheme_label = cTk.CTkLabel(self, text="Color Scheme:", fg_color=StartWindow.COLOR_BACKGROUND, text_color=StartWindow.COLOR_TEXT)
        self.color_scheme_label.place(relx=0.5, rely=0.65, anchor="center")

        self.color_scheme_button = cTk.CTkButton(self, fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
        self.color_scheme_button.place(relx=0.5, rely=0.72, anchor="center")

        self.get_color_schemes()  # Load available color schemes

        self.color_scheme_dropdown = CTkScrollableDropdown(self.color_scheme_button, values=COLOR_SCHEMES, command=lambda color_scheme: set_color_scheme(color_scheme), fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT, button_color=StartWindow.COLOR_BUTTON, scrollbar=True, height=200)

        # Save button
        self.save_button = cTk.CTkButton(self, text="Save Settings", command=lambda: save_and_close(self), fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
        self.save_button.place(relx=0.5, rely=0.8, anchor="center")
    
    def get_color_schemes(self):
        """## Loads available color schemes from a JSON file."""
        from utilities.game import Game
        from interactions import resource_path
        global COLOR_SCHEMES
        with open(resource_path("resources/json/color_schemes.json"), "r") as color_scheme_file:
            schemes = json.load(color_scheme_file)
            COLOR_SCHEMES = list(schemes.keys())
        self.color_scheme_button.configure(text=Game.color_scheme)
