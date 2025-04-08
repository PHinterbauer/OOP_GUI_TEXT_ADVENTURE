# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/interaction.py
# Interacting with the GUI
# ====================================

import customtkinter as cTk
import time
import json

from gui.design import SettingsWindow, MainWindow, InventoryWindow, StartWindow

# Global instances
SettingsWindowInstance = None
root = None
InventoryWindowInstance = None 

def open_start_menu(MainWindowInstance):
    """## Opens the start menu
    Minimizes the main window and shows the start menu.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
    """
    MainWindowInstance.master.deiconify()
    MainWindowInstance.withdraw()

def open_main_window(StartWindowInstance):
    """## Opens the main game window
    Validates the player's name and opens the main game window.

    Args:
        StartWindowInstance (StartWindow): The start menu window instance.
    """
    from utilities.game import Game
    if StartWindowInstance.player_name.strip() != "":
        StartWindowInstance.withdraw() 
        if not Game.MainWindowInstance:  
            Game.MainWindowInstance = MainWindow(StartWindowInstance, open_inventory, open_start_menu)
        else:
            Game.MainWindowInstance.deiconify() 
    else:
        StartWindowInstance.info_label.configure(text="Bitte gib einen Namen ein!")

def open_inventory(MainWindowInstance):
    """## Opens the inventory window
    Opens the inventory window or focuses on it if already open.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
    """
    global InventoryWindowInstance
    from utilities.game import Game
    if InventoryWindowInstance is None or not InventoryWindowInstance.winfo_exists():
        MainWindowInstance.withdraw()
        InventoryWindowInstance = InventoryWindow(MainWindowInstance, close_inventory)
        update_inventory_table(InventoryWindowInstance, Game.main_character.inventory)
    else:
        InventoryWindowInstance.focus()

def open_settings(parent):
    """## Opens the settings window
    Opens the settings window or focuses on it if already open.

    Args:
        parent (MainWindow or StartWindow): The parent window instance.
    """
    global SettingsWindowInstance
    if SettingsWindowInstance is None or not SettingsWindowInstance.winfo_exists():
        SettingsWindowInstance = SettingsWindow(parent, save_and_close, set_color_scheme)
        SettingsWindowInstance.grab_set()
        SettingsWindowInstance.focus()
        SettingsWindowInstance.lift()
    else:
        SettingsWindowInstance.focus()
        SettingsWindowInstance.lift()

def close_inventory(InventoryWindowInstance):
    """## Closes the inventory window
    Restores the main window and closes the inventory window.

    Args:
        InventoryWindowInstance (InventoryWindow): The inventory window instance.
    """
    InventoryWindowInstance.master.deiconify()
    InventoryWindowInstance.destroy()

def close_settings():
    """## Closes the settings window
    Destroys the settings window instance."""
    global SettingsWindowInstance
    if SettingsWindowInstance is not None and SettingsWindowInstance.winfo_exists():
        SettingsWindowInstance.destroy()
        SettingsWindowInstance = None

def confirm_player_name(StartWindowInstance):
    """## Confirms the player's name
    Validates and sets the player's name.

    Args:
        StartWindowInstance (StartWindow): The start menu window instance.
    """
    StartWindowInstance.player_name = StartWindowInstance.player_name_entry.get()
    if StartWindowInstance.player_name.strip() != "":
        if len(StartWindowInstance.player_name) > 0 and len(StartWindowInstance.player_name) <= 15:
            StartWindowInstance.info_label.configure(text=f"Der Name deines Charakters lautet {StartWindowInstance.player_name}!")
        else:
            StartWindowInstance.info_label.configure(text="Der Name darf nicht 0 Zeichen oder länger als 15 Zeichen sein!")
    else:
        StartWindowInstance.info_label.configure(text="Bitte gib einen Namen ein!")

def add_text_to_textbox(MainWindowInstance, in_str: str, callback=None):
    """## Adds text to the textbox
    Adds a string to the main window's textbox.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        in_str (str): The string to add.
        callback (function, optional): Callback to execute after adding text.
    """
    if in_str:
        MainWindowInstance.text_box.configure(state="normal")
        MainWindowInstance.text_box.insert("end", in_str + "\n")
        MainWindowInstance.text_box.update_idletasks()
        MainWindowInstance.text_box.see("end")
        MainWindowInstance.text_box.configure(state="disabled")
        if callback:
            MainWindowInstance.after(100, callback)  # Callback after text addition

def add_text_to_textbox_slow(MainWindowInstance, in_str: str, delay=0.05, callback=None):
    """## Adds text to the textbox slowly
    Adds a string to the main window's textbox character by character.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        in_str (str): The string to add.
        delay (float, optional): Delay between characters. Defaults to 0.05.
        callback (function, optional): Callback to execute after adding text.
    """
    if in_str:
        MainWindowInstance.text_box.configure(state="normal")
        for char in in_str:
            MainWindowInstance.text_box.insert("end", char)
            MainWindowInstance.text_box.update_idletasks()
            time.sleep(delay)
        MainWindowInstance.text_box.insert("end", "\n")
        MainWindowInstance.text_box.see("end")
        MainWindowInstance.text_box.configure(state="disabled")
        if callback:
            MainWindowInstance.after(100, callback)  # Callback after slow text addition

def add_list_to_textbox(MainWindowInstance, in_list: list, callback=None):
    """## Adds a list of items to the textbox
    Adds each item in the list as a new line in the main window's textbox.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        in_list (list): The list of strings to add.
        callback (function, optional): Callback to execute after adding the list.
    """
    if in_list:
        MainWindowInstance.text_box.configure(state="normal")
        for item in in_list:
            line = f'{item}\n'
            MainWindowInstance.text_box.insert("end", line)
            MainWindowInstance.text_box.update_idletasks()
            MainWindowInstance.text_box.see("end")
        MainWindowInstance.text_box.configure(state="disabled")
        if callback:
            MainWindowInstance.after(100, callback)  # Callback after adding the list

def add_list_to_textbox_slow(MainWindowInstance, in_list: list, delay=0.05, callback=None):
    """## Adds a list of items to the textbox slowly
    Adds each item in the list character by character with a delay.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        in_list (list): The list of strings to add.
        delay (float, optional): Delay between characters. Defaults to 0.05.
        callback (function, optional): Callback to execute after adding the list.
    """
    if in_list:
        MainWindowInstance.text_box.configure(state="normal")
        for item in in_list:
            line = f'{item}\n'
            for char in line:
                MainWindowInstance.text_box.insert("end", char)
                MainWindowInstance.text_box.update_idletasks()
                time.sleep(delay)
            MainWindowInstance.text_box.see("end")
        MainWindowInstance.text_box.configure(state="disabled")
        if callback:
            MainWindowInstance.after(100, callback)  # Callback after slow addition

def add_dict_to_textbox(MainWindowInstance, in_dict: dict, callback=None):
    """## Adds a dictionary to the textbox
    Adds each key-value pair in the dictionary as a new line in the main window's textbox.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        in_dict (dict): The dictionary to add.
        callback (function, optional): Callback to execute after adding the dictionary.
    """
    if in_dict:
        MainWindowInstance.text_box.configure(state="normal")
        for key, value in in_dict.items():
            line = f"{key}: {value}\n"
            MainWindowInstance.text_box.insert("end", line)
            MainWindowInstance.text_box.update_idletasks()
            MainWindowInstance.text_box.see("end")
        MainWindowInstance.text_box.configure(state="disabled")
        if callback:
            MainWindowInstance.after(100, callback)  # Callback after adding the dictionary

def add_dict_to_textbox_slow(MainWindowInstance, in_dict: dict, delay=0.05, callback=None):
    """## Adds a dictionary to the textbox slowly
    Adds each key-value pair in the dictionary character by character with a delay.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        in_dict (dict): The dictionary to add.
        delay (float, optional): Delay between characters. Defaults to 0.05.
        callback (function, optional): Callback to execute after adding the dictionary.
    """
    if in_dict:
        MainWindowInstance.text_box.configure(state="normal")
        for key, value in in_dict.items():
            line = f"{key}: {value}\n"
            for char in line:
                MainWindowInstance.text_box.insert("end", char)
                MainWindowInstance.text_box.update_idletasks()
                time.sleep(delay)
            MainWindowInstance.text_box.see("end")
        MainWindowInstance.text_box.configure(state="disabled")
        if callback:
            MainWindowInstance.after(100, callback)  # Callback after slow addition

def delete_all_entries(MainWindowInstance):
    """## Deletes all entries in the textbox
    Clears the main window's textbox.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
    """
    MainWindowInstance.text_box.configure(state="normal")
    MainWindowInstance.text_box.delete("0.0", "end")
    MainWindowInstance.text_box.configure(state="disabled")

def add_choice_button(MainWindowInstance, text, callback):
    """## Adds a choice button
    Adds a button to the choice frame in the main window.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        text (str): The button text.
        callback (function): Callback to execute when the button is clicked.
    """
    choice_button = cTk.CTkButton(MainWindowInstance.choice_frame, text=text, command=lambda: callback(), fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
    choice_button.pack(side="top", fill="x", padx=5, pady=5)

def delete_choice_buttons(MainWindowInstance):
    """## Deletes all choice buttons
    Removes all buttons from the choice frame in the main window.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
    """
    for widget in MainWindowInstance.choice_frame.winfo_children():
        widget.destroy()

def read_choice_buttons(MainWindowInstance, choice, callback=None):
    """## Reads the selected choice button
    Returns the selected choice and optionally executes a callback.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        choice (str): The selected choice.
        callback (function, optional): Callback to execute after reading the choice.

    Returns:
        str: The selected choice.
    """
    if callback:
        MainWindowInstance.after(100, lambda: callback(choice))  # Callback after reading the choice
    return choice

def gui_input(MainWindowInstance, gui_input_callback, label_text, y_position=0.58, callback=None):
    """## Creates a GUI input field
    Adds an input field to the main window for user input.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        gui_input_callback (function): Callback to handle the input value.
        label_text (str): The label text for the input field.
        y_position (float, optional): Y position of the input field. Defaults to 0.58.
        callback (function, optional): Callback to execute after input is handled.
    """
    input_label = cTk.CTkLabel(MainWindowInstance, text=label_text)
    input_label.place(relx=0.475, rely=y_position, relwidth=0.85, anchor="center")
    input_entry = cTk.CTkEntry(MainWindowInstance, fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT)
    input_entry.place(relx=0.475, rely=y_position + 0.05, relwidth=0.85, anchor="center")
    input_entry.focus_set()

    def handle_input(event):
        """Handles the input value when Enter is pressed."""
        input_value = input_entry.get()
        input_entry.delete(0, "end")
        input_entry.destroy()
        input_label.destroy()
        MainWindowInstance.input_callback_value = gui_input_callback(MainWindowInstance, input_value)
        if callback:
            MainWindowInstance.after(100, lambda: callback(input_value))  # Callback after input handling

    input_entry.bind("<Return>", handle_input)

def gui_save_input_value(MainWindowInstance, input_value, callback=None):
    """## Saves the input value from the GUI
    Saves the input value and optionally executes a callback.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        input_value (str): The input value to save.
        callback (function, optional): Callback to execute after saving the input value.

    Returns:
        str: The saved input value.
    """
    if callback:
        MainWindowInstance.after(100, lambda: callback(input_value))  # Callback after saving the input value
    return input_value

def update_stats_table(MainWindowInstance, attributes: dict):
    """## Updates the stats table
    Updates the stats table in the main window with the given attributes.

    Args:
        MainWindowInstance (MainWindow): The main game window instance.
        attributes (dict): The attributes to display in the stats table.
    """
    # Clear existing widgets in the stats table
    for widget in MainWindowInstance.stats_table_frame.winfo_children():
        widget.destroy()
    # Add headers for the stats table
    header_key = cTk.CTkLabel(MainWindowInstance.stats_table_frame, text="Attribut", fg_color=StartWindow.COLOR_BUTTON, text_color=StartWindow.COLOR_TEXT, anchor="center", padx=5, pady=5)
    header_key.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    header_value = cTk.CTkLabel(MainWindowInstance.stats_table_frame, text="Wert", fg_color=StartWindow.COLOR_BUTTON, text_color=StartWindow.COLOR_TEXT, anchor="center", padx=5, pady=5)
    header_value.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
    # Add each attribute as a row in the stats table
    for row, (key, value) in enumerate(attributes.items(), start=1):
        key_label = cTk.CTkLabel(MainWindowInstance.stats_table_frame, text=key, fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT, anchor="center", padx=5, pady=5)
        key_label.grid(row=row, column=0, sticky="nsew", padx=2, pady=2)
        value_label = cTk.CTkLabel(MainWindowInstance.stats_table_frame, text=str(value), fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT, anchor="center", padx=5, pady=5)
        value_label.grid(row=row, column=1, sticky="nsew", padx=2, pady=2)
    # Configure row and column weights for resizing
    for i in range(len(attributes) + 1):
        MainWindowInstance.stats_table_frame.grid_rowconfigure(i, weight=1)
    MainWindowInstance.stats_table_frame.grid_columnconfigure(0, weight=1)
    MainWindowInstance.stats_table_frame.grid_columnconfigure(1, weight=1)

def update_inventory_table(InventoryWindowInstance, inventory: dict):
    """## Updates the inventory table
    Updates the inventory table in the inventory window with the given items.

    Args:
        InventoryWindowInstance (InventoryWindow): The inventory window instance.
        inventory (dict): The inventory items to display.
    """
    # Clear existing widgets in the inventory table
    for widget in InventoryWindowInstance.inventory_table_frame.winfo_children():
        widget.destroy()
    # Add headers for the inventory table
    header_border_frame = cTk.CTkFrame(InventoryWindowInstance.inventory_table_frame, fg_color=StartWindow.COLOR_BACKGROUND)
    header_border_frame.place(relx=0.04, rely=0.04, relwidth=0.87, relheight=0.12)
    header_key = cTk.CTkLabel(InventoryWindowInstance.inventory_table_frame, text="Gegenstand", fg_color=StartWindow.COLOR_BUTTON, text_color=StartWindow.COLOR_TEXT, anchor="center", padx=5, pady=5, height=30)
    header_key.place(relx=0.05, relwidth=0.4, relheight=0.1, rely=0.05)
    header_value = cTk.CTkLabel(InventoryWindowInstance.inventory_table_frame, text="Anzahl", fg_color=StartWindow.COLOR_BUTTON, text_color=StartWindow.COLOR_TEXT, anchor="center", padx=5, pady=5, height=30)
    header_value.place(relx=0.5, relwidth=0.4, relheight=0.1, rely=0.05)
    # Add each inventory item as a row in the inventory table
    if inventory:
        for index, (key, value) in enumerate(inventory.items(), start=1):
            item_border_frame = cTk.CTkFrame(InventoryWindowInstance.inventory_table_frame, fg_color=StartWindow.COLOR_BACKGROUND)
            item_border_frame.place(relx=0.045, rely=0.19 + index * 0.1, relwidth=0.86, relheight=0.12)
            key_label = cTk.CTkLabel(InventoryWindowInstance.inventory_table_frame, text=key, fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT, anchor="center", padx=5, pady=5)
            key_label.place(relx=0.05, rely=0.2 + index * 0.1, relwidth=0.4, relheight=0.1)
            value_label = cTk.CTkLabel(InventoryWindowInstance.inventory_table_frame, text=str(value), fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT, anchor="center", padx=5, pady=5)
            value_label.place(relx=0.5, rely=0.2 + index * 0.1, relwidth=0.4, relheight=0.1)
    else:
        # Display a message if the inventory is empty
        label_if_empty = cTk.CTkLabel(InventoryWindowInstance, text="Dein Inventar ist leer!", fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT, anchor="center", padx=5, pady=5)
        label_if_empty.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)

def load_color_scheme(color_scheme_name):
    """## Loads a color scheme
    Loads the color scheme from the JSON file and applies it.

    Args:
        color_scheme_name (str): The name of the color scheme to load.
    """
    with open("./resources/json/color_schemes.json", "r") as color_scheme_file:
        schemes = json.load(color_scheme_file)
        if color_scheme_name in schemes:
            # Apply color scheme to global variables
            StartWindow.COLOR_BUTTON = schemes[color_scheme_name]["COLOR_BUTTON"]
            StartWindow.COLOR_BACKGROUND = schemes[color_scheme_name]["COLOR_BACKGROUND"]
            StartWindow.COLOR_TEXT = schemes[color_scheme_name]["COLOR_TEXT"]
            StartWindow.COLOR_BUTTON_HOVER = schemes[color_scheme_name]["COLOR_BUTTON_HOVER"]
            StartWindow.COLOR_FRAME = schemes[color_scheme_name]["COLOR_FRAME"]

def set_color_scheme(color_scheme):
    """## Sets the color scheme
    Updates the global color scheme variable.

    Args:
        color_scheme (str): The name of the color scheme to set.
    """
    from utilities.game import Game
    Game.color_scheme = color_scheme

def update_color_scheme():
    """## Updates the color scheme
    Applies the current color scheme to all GUI elements.
    """
    from utilities.game import Game
    global root, InventoryWindowInstance
    # Update root window
    if root and root.winfo_exists():
        root.configure(fg_color=StartWindow.COLOR_BACKGROUND)
        for widget in root.winfo_children():
            if isinstance(widget, cTk.CTkLabel):
                widget.configure(fg_color=StartWindow.COLOR_BACKGROUND, text_color=StartWindow.COLOR_TEXT)
            elif isinstance(widget, cTk.CTkButton):
                widget.configure(fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
            elif isinstance(widget, cTk.CTkEntry):
                widget.configure(fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT)
            elif isinstance(widget, cTk.CTkFrame):
                widget.configure(fg_color=StartWindow.COLOR_FRAME)
    # Update MainWindowInstance
    if Game.MainWindowInstance and Game.MainWindowInstance.winfo_exists():
        Game.MainWindowInstance.configure(fg_color=StartWindow.COLOR_BACKGROUND)
        for widget in Game.MainWindowInstance.winfo_children():
            if isinstance(widget, cTk.CTkLabel):
                widget.configure(fg_color=StartWindow.COLOR_BACKGROUND, text_color=StartWindow.COLOR_TEXT)
            elif isinstance(widget, cTk.CTkButton):
                widget.configure(fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
            elif isinstance(widget, cTk.CTkTextbox):
                widget.configure(fg_color=StartWindow.COLOR_FRAME, text_color=StartWindow.COLOR_TEXT)
            elif isinstance(widget, cTk.CTkFrame):
                widget.configure(fg_color=StartWindow.COLOR_FRAME)
    # Update InventoryWindowInstance
    if InventoryWindowInstance and InventoryWindowInstance.winfo_exists():
        InventoryWindowInstance.configure(fg_color=StartWindow.COLOR_BACKGROUND)
        for widget in InventoryWindowInstance.winfo_children():
            if isinstance(widget, cTk.CTkLabel):
                widget.configure(fg_color=StartWindow.COLOR_BACKGROUND, text_color=StartWindow.COLOR_TEXT)
            elif isinstance(widget, cTk.CTkButton):
                widget.configure(fg_color=StartWindow.COLOR_BUTTON, hover_color=StartWindow.COLOR_BUTTON_HOVER, text_color=StartWindow.COLOR_TEXT)
            elif isinstance(widget, cTk.CTkFrame):
                widget.configure(fg_color=StartWindow.COLOR_FRAME)

def load_settings():
    """## Loads game settings
    Reads settings from a JSON file and applies them.
    """
    from utilities.game import Game
    try:
        with open("./resources/json/settings.json", "r") as settings_file:
            settings_data = json.load(settings_file)
            # Apply settings to global variables
            Game.gui_mode = settings_data.get("Game.gui_mode", True)
            Game.sleep_time = settings_data.get("Game.sleep_time", 0.04)
            Game.separator_length = settings_data.get("Game.separator_length", 30)
            Game.color_scheme = settings_data.get("Game.color_scheme", "Default")
            load_color_scheme(Game.color_scheme)
    except FileNotFoundError:
        # Default settings if file is not found
        Game.gui_mode = True
        Game.sleep_time = 0.04
        Game.separator_length = 320
        Game.color_scheme = "Default"
        settings_data = {
            "Game.gui_mode": Game.gui_mode,
            "Game.sleep_time": Game.sleep_time,
            "Game.separator_length": Game.separator_length,
            "Game.color_scheme": Game.color_scheme,
        }
        with open("./resources/json/settings.json", "w") as settings_file:
            json.dump(settings_data, settings_file, indent=4)
        load_color_scheme(Game.color_scheme)

def save_settings(gui_mode_switch, sleep_time_entry, separator_length_entry, selected_color_scheme):
    """## Saves game settings
    Writes the current settings to a JSON file.

    Args:
        gui_mode_switch (CTkSwitch): The GUI mode switch widget.
        sleep_time_entry (CTkEntry): The sleep time entry widget.
        separator_length_entry (CTkEntry): The separator length entry widget.
        selected_color_scheme (str): The selected color scheme.
    """
    gui_mode = gui_mode_switch.get()
    sleep_time = float(sleep_time_entry.get()) if sleep_time_entry.get() else 0.04
    separator_length = int(separator_length_entry.get()) if separator_length_entry.get() else 120
    settings_data = {
        "Game.gui_mode": gui_mode,
        "Game.sleep_time": sleep_time,
        "Game.separator_length": separator_length,
        "Game.color_scheme": selected_color_scheme,
    }
    with open("./resources/json/settings.json", "w") as settings_file:
        json.dump(settings_data, settings_file, indent=4)

def save_and_close(SettingsWindowInstance):
    """## Saves settings and closes the settings window
    Saves the current settings and updates the color scheme.

    Args:
        SettingsWindowInstance (SettingsWindow): The settings window instance.
    """
    from utilities.game import Game
    selected_color_scheme = Game.color_scheme
    save_settings(SettingsWindowInstance.gui_mode_switch, SettingsWindowInstance.sleep_time_entry, SettingsWindowInstance.separator_length_entry, selected_color_scheme)
    load_color_scheme(selected_color_scheme)
    update_color_scheme()
    close_settings()

def gui_initialize():
    """## Initializes the GUI
    Sets up the root window and starts the GUI main loop.
    """
    from utilities.game import Game
    global root
    root = StartWindow(open_main_window, confirm_player_name, open_settings)
    root.after(100, Game.wait_for_main_window)  # Callback to wait for the main window
    root.mainloop()
