# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/interaction.py
# Interacting with the GUI
# ====================================

import customtkinter as cTk
import time
import json

from gui.design import SettingsWindow, MainWindow, InventoryWindow, StartWindow

SettingsWindowInstance = None
root = None

def open_start_menu(MainWindowInstance):
    MainWindowInstance.master.deiconify()
    MainWindowInstance.destroy()

def open_main_window(StartWindowInstance):
    from utilities.game import Game
    if StartWindowInstance.player_name.strip() != "":
        StartWindowInstance.withdraw()
        Game.MainWindowInstance = MainWindow(StartWindowInstance, open_inventory, open_start_menu)
    else:
        StartWindowInstance.info_label.configure(text="Bitte gib einen Namen ein!")

def open_inventory(MainWindowInstance):
    MainWindowInstance.withdraw()
    InventoryWindow(MainWindowInstance, close_inventory)

def open_settings(parent):
    global SettingsWindowInstance
    if SettingsWindowInstance is None or not SettingsWindowInstance.winfo_exists():
        SettingsWindowInstance = SettingsWindow(parent, save_and_close)
        SettingsWindowInstance.grab_set()
    else:
        SettingsWindowInstance.focus()

def close_inventory(InventoryWindowInstance):
    InventoryWindowInstance.master.deiconify()
    InventoryWindowInstance.destroy()

def close_settings():
    global SettingsWindowInstance
    if SettingsWindowInstance is not None and SettingsWindowInstance.winfo_exists():
        SettingsWindowInstance.destroy()
        SettingsWindowInstance = None

def confirm_player_name(StartWindowInstance):
    StartWindowInstance.player_name = StartWindowInstance.player_name_entry.get()
    if StartWindowInstance.player_name.strip() != "":
        if len(StartWindowInstance.player_name) > 0 and len(StartWindowInstance.player_name) <= 15:
            StartWindowInstance.info_label.configure(text=f"Der Name deines Charakters lautet {StartWindowInstance.player_name}!")
        else:
            StartWindowInstance.info_label.configure(text="Der Name darf nicht 0 Zeichen oder länger als 15 Zeichen sein!")
    else:
        StartWindowInstance.info_label.configure(text="Bitte gib einen Namen ein!")

def add_text_to_textbox(MainWindowInstance, text: str):
    """Adds text to the textbox immediately."""
    MainWindowInstance.text_box.configure(state="normal")
    MainWindowInstance.text_box.insert("end", text + "\n")
    MainWindowInstance.text_box.update_idletasks()
    MainWindowInstance.text_box.configure(state="disabled")

def add_text_to_textbox_slow(MainWindowInstance, text: list, delay=0.05, callback=None):
    """Adds text to the textbox slowly and executes a callback after."""
    MainWindowInstance.text_box.configure(state="normal")
    for line in text:
        for char in line:
            MainWindowInstance.text_box.insert("end", char)
            MainWindowInstance.text_box.update_idletasks()
            time.sleep(delay)
        MainWindowInstance.text_box.insert("end", "\n")
    MainWindowInstance.text_box.configure(state="disabled")

def add_dict_to_textbox_slow(MainWindowInstance, in_dict: dict, delay=0.05, callback=None):
    """Adds a dictionary to the textbox slowly and executes a callback after."""
    if in_dict:
        MainWindowInstance.text_box.configure(state="normal")
        keys = list(in_dict.keys())
        values = list(in_dict.values())

        def type_dict(index=0):
            if index < len(keys):
                line = f"{keys[index]}: {values[index]}\n"
                MainWindowInstance.text_box.insert("end", line)
                MainWindowInstance.update_idletasks()
                MainWindowInstance.after(int(delay * 1000), lambda: type_dict(index + 1))
            else:
                MainWindowInstance.text_box.configure(state="disabled")
                if callback:
                    MainWindowInstance.after(100, callback)

        type_dict()

def add_dict_to_textbox(MainWindowInstance, in_dict: dict):
    if in_dict:
        MainWindowInstance.text_box.configure(state="normal")
        for key, value in in_dict.items():
            line = f"{key}: {value}\n"
            MainWindowInstance.text_box.insert("end", line)
            MainWindowInstance.text_box.update_idletasks()
        MainWindowInstance.text_box.configure(state="disabled")

def add_list_to_textbox(MainWindowInstance, in_list: list, callback=None):
    """Adds a list to the textbox and executes a callback after."""
    if in_list:
        MainWindowInstance.text_box.configure(state="normal")
        for item in in_list:
            # Append each item as a new line
            line = f"{item}\n"
            for char in line:
                MainWindowInstance.text_box.insert("end", char)
                
                MainWindowInstance.text_box.update_idletasks()
                time.sleep(0.05)
            MainWindowInstance.text_box.see("end")
        MainWindowInstance.text_box.configure(state="disabled")
        if callback:
            MainWindowInstance.after(100, callback)

def delete_all_entries(MainWindowInstance):
    MainWindowInstance.text_box.configure(state="normal")
    MainWindowInstance.text_box.delete("0.0", "end")
    MainWindowInstance.text_box.configure(state="disabled")

def add_choice_button(MainWindowInstance, text, callback):
    """Adds a choice button to the GUI."""
    choice_button = cTk.CTkButton(
        MainWindowInstance.choice_frame,
        text=text,
        command=lambda: callback()
    )
    choice_button.pack(side="top", fill="x", padx=5, pady=5)

def delete_choice_buttons(MainWindowInstance):
    for widget in MainWindowInstance.choice_frame.winfo_children():
        widget.destroy()

def read_choice_buttons(MainWindowInstance, choice, callback=None):
    """Reads the choice buttons and executes a callback after."""
    MainWindowInstance.delete_choice_buttons()
    if callback:
        MainWindowInstance.after(100, lambda: callback(choice))
    return choice

def gui_input(MainWindowInstance, gui_input_callback, label_text, y_position=0.58, callback=None):
    """Creates an input field and executes a callback after input is handled."""
    input_label = cTk.CTkLabel(MainWindowInstance, text=label_text)
    input_label.place(relx=0.475, rely=y_position, relwidth=0.85, anchor="center")
    input_entry = cTk.CTkEntry(MainWindowInstance)
    input_entry.place(relx=0.475, rely=y_position + 0.05, relwidth=0.85, anchor="center")
    input_entry.focus_set()

    def handle_input(event):
        input_value = input_entry.get()
        input_entry.delete(0, "end")
        input_entry.destroy()
        input_label.destroy()
        MainWindowInstance.input_callback_value = gui_input_callback(MainWindowInstance, input_value)
        if callback:
            MainWindowInstance.after(100, lambda: callback(input_value))

    input_entry.bind("<Return>", handle_input)

def gui_save_input_value(MainWindowInstance, input_value, callback=None):
    """Saves the input value and executes a callback."""
    if callback:
        MainWindowInstance.after(100, lambda: callback(input_value))
    return input_value

def load_settings():
    from utilities.game import Game
    try:
        with open("./resources/json/settings.json", "r") as settings_file:
            settings_data = json.load(settings_file)
            Game.gui_mode = settings_data.get("Game.gui_mode", True)
            Game.sleep_time = settings_data.get("Game.sleep_time", 0.04)
            Game.separator_length = settings_data.get("Game.separator_length", 120)
    except FileNotFoundError:
        Game.gui_mode = True
        Game.sleep_time = 0.04
        Game.separator_length = 120
        settings_data = {
        "Game.gui_mode": Game.gui_mode,
        "Game.sleep_time": Game.sleep_time,
        "Game.separator_length": Game.separator_length,
        }
        with open("./resources/json/settings.json", "w") as settings_file:
            json.dump(settings_data, settings_file, indent=4)

def save_settings(gui_mode_switch, sleep_time_entry, separator_length_entry):
    gui_mode = gui_mode_switch.get()
    sleep_time = float(sleep_time_entry.get()) if sleep_time_entry.get() else 0.04
    separator_length = int(separator_length_entry.get()) if separator_length_entry.get() else 120
    settings_data = {
        "Game.gui_mode": gui_mode,
        "Game.sleep_time": sleep_time,
        "Game.separator_length": separator_length,
    }
    with open("./resources/json/settings.json", "w") as settings_file:
        json.dump(settings_data, settings_file, indent=4)

def save_and_close(SettingsWindowInstance):
    save_settings(SettingsWindowInstance.gui_mode_switch, SettingsWindowInstance.sleep_time_entry, SettingsWindowInstance.separator_length_entry)
    close_settings()

def gui_initialize():
    from utilities.game import Game
    global root
    root = StartWindow(open_main_window, confirm_player_name, open_settings)
    root.after(100, Game.wait_for_main_window)
    root.mainloop()
