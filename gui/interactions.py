# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/interaction.py
# Interacting with the GUI
# ====================================

import customtkinter as cTk
import time
import json

from gui.design import SettingsWindow, MainWindow, InventoryWindow, StartWindow, COLOR_BUTTON, COLOR_FRAME, COLOR_TEXT

SettingsWindowInstance = None
root = None
InventoryWindowInstance = None 

def open_start_menu(MainWindowInstance):
    MainWindowInstance.master.deiconify()
    MainWindowInstance.withdraw()

def open_main_window(StartWindowInstance):
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
    global InventoryWindowInstance
    from utilities.game import Game
    if InventoryWindowInstance is None or not InventoryWindowInstance.winfo_exists():
        MainWindowInstance.withdraw()
        InventoryWindowInstance = InventoryWindow(MainWindowInstance, close_inventory)
        update_inventory_table(InventoryWindowInstance, Game.main_character.inventory)
    else:
        InventoryWindowInstance.focus()

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

def add_text_to_textbox(MainWindowInstance, in_str: str, callback=None):
    if in_str:
        MainWindowInstance.text_box.configure(state="normal")
        MainWindowInstance.text_box.insert("end", in_str + "\n")
        MainWindowInstance.text_box.update_idletasks()
        MainWindowInstance.text_box.see("end")
        MainWindowInstance.text_box.configure(state="disabled")
        if callback:
            MainWindowInstance.after(100, callback)

def add_text_to_textbox_slow(MainWindowInstance, in_str: str, delay=0.05, callback=None):
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
            MainWindowInstance.after(100, callback)

def add_list_to_textbox(MainWindowInstance, in_list: list, callback=None):
    if in_list:
        MainWindowInstance.text_box.configure(state="normal")
        for item in in_list:
            line = f'{item}\n'
            MainWindowInstance.text_box.insert("end", line)
            MainWindowInstance.text_box.update_idletasks()
            MainWindowInstance.text_box.see("end")
        MainWindowInstance.text_box.configure(state="disabled")
        if callback:
            MainWindowInstance.after(100, callback)

def add_list_to_textbox_slow(MainWindowInstance, in_list: list, delay=0.05, callback=None):
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
            MainWindowInstance.after(100, callback)

def add_dict_to_textbox(MainWindowInstance, in_dict: dict, callback=None):
    if in_dict:
        MainWindowInstance.text_box.configure(state="normal")
        for key, value in in_dict.items():
            line = f"{key}: {value}\n"
            MainWindowInstance.text_box.insert("end", line)
            MainWindowInstance.text_box.update_idletasks()
            MainWindowInstance.text_box.see("end")
        MainWindowInstance.text_box.configure(state="disabled")
        if callback:
            MainWindowInstance.after(100, callback)

def add_dict_to_textbox_slow(MainWindowInstance, in_dict: dict, delay=0.05, callback=None):
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
            MainWindowInstance.after(100, callback)

def delete_all_entries(MainWindowInstance):
    MainWindowInstance.text_box.configure(state="normal")
    MainWindowInstance.text_box.delete("0.0", "end")
    MainWindowInstance.text_box.configure(state="disabled")

def add_choice_button(MainWindowInstance, text, callback):
    choice_button = cTk.CTkButton(MainWindowInstance.choice_frame, text=text, command=lambda: callback())
    choice_button.pack(side="top", fill="x", padx=5, pady=5)

def delete_choice_buttons(MainWindowInstance):
    for widget in MainWindowInstance.choice_frame.winfo_children():
        widget.destroy()

def read_choice_buttons(MainWindowInstance, choice, callback=None):
    MainWindowInstance.delete_choice_buttons()
    if callback:
        MainWindowInstance.after(100, lambda: callback(choice))
    return choice

def gui_input(MainWindowInstance, gui_input_callback, label_text, y_position=0.58, callback=None):
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
    if callback:
        MainWindowInstance.after(100, lambda: callback(input_value))
    return input_value

def update_stats_table(MainWindowInstance, attributes: dict):
    for widget in MainWindowInstance.stats_table_frame.winfo_children():
        widget.destroy()
    header_key = cTk.CTkLabel(MainWindowInstance.stats_table_frame, text="Attribut", fg_color=COLOR_BUTTON, text_color=COLOR_TEXT, anchor="center", padx=5, pady=5)
    header_key.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    header_value = cTk.CTkLabel(MainWindowInstance.stats_table_frame, text="Wert", fg_color=COLOR_BUTTON, text_color=COLOR_TEXT, anchor="center", padx=5, pady=5)
    header_value.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
    for row, (key, value) in enumerate(attributes.items(), start=1):
        key_label = cTk.CTkLabel(MainWindowInstance.stats_table_frame, text=key, fg_color=COLOR_FRAME, text_color=COLOR_TEXT, anchor="center", padx=5, pady=5)
        key_label.grid(row=row, column=0, sticky="nsew", padx=2, pady=2)
        value_label = cTk.CTkLabel(MainWindowInstance.stats_table_frame, text=str(value), fg_color=COLOR_FRAME, text_color=COLOR_TEXT, anchor="center", padx=5, pady=5)
        value_label.grid(row=row, column=1, sticky="nsew", padx=2, pady=2)
    for i in range(len(attributes) + 1):
        MainWindowInstance.stats_table_frame.grid_rowconfigure(i, weight=1)
    MainWindowInstance.stats_table_frame.grid_columnconfigure(0, weight=1)
    MainWindowInstance.stats_table_frame.grid_columnconfigure(1, weight=1)

def update_inventory_table(InventoryWindowInstance, inventory: dict):
    for widget in InventoryWindowInstance.inventory_table_frame.winfo_children():
        widget.destroy()
    header_key = cTk.CTkLabel(InventoryWindowInstance.inventory_table_frame, text="Gegenstand", fg_color=COLOR_BUTTON, text_color=COLOR_TEXT, anchor="center", padx=5, pady=5, height=30)
    header_key.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    header_value = cTk.CTkLabel(InventoryWindowInstance.inventory_table_frame, text="Anzahl", fg_color=COLOR_BUTTON, text_color=COLOR_TEXT, anchor="center", padx=5, pady=5, height=30)
    header_value.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
    if inventory:
        for row, (key, value) in enumerate(inventory.items(), start=1):
            key_label = cTk.CTkLabel(InventoryWindowInstance.inventory_table_frame, text=key, fg_color=COLOR_FRAME, text_color=COLOR_TEXT, anchor="center", padx=5, pady=5)
            key_label.grid(row=row, column=0, sticky="nsew", padx=2, pady=2)
            value_label = cTk.CTkLabel(InventoryWindowInstance.inventory_table_frame, text=str(value), fg_color=COLOR_FRAME, text_color=COLOR_TEXT, anchor="center", padx=5, pady=5)
            value_label.grid(row=row, column=1, sticky="nsew", padx=2, pady=2)
        for i in range(len(inventory) + 1):
            InventoryWindowInstance.inventory_table_frame.grid_rowconfigure(i, weight=1)
        InventoryWindowInstance.inventory_table_frame.grid_columnconfigure(0, weight=1)
        InventoryWindowInstance.inventory_table_frame.grid_columnconfigure(1, weight=1)
    else:
        label_if_empty = cTk.CTkLabel(InventoryWindowInstance, text="Dein Inventar ist leer!", fg_color=COLOR_FRAME, text_color=COLOR_TEXT, anchor="center", padx=5, pady=5)
        label_if_empty.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.1, anchor="center")

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
