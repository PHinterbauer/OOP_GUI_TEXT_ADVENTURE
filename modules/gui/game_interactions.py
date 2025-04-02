# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/game_helpers.py
# Helper functions for the GUI in game
# ====================================

import customtkinter as cTk
import time
import json

def add_text_to_textbox(MainWindowInstance, text: str):
    if text != "":
        MainWindowInstance.text_box.configure(state="normal")
        MainWindowInstance.text_box.insert("1.0", text + "\n")
        separator = cTk.CTkFrame(MainWindowInstance.text_box, width=MainWindowInstance.text_box._textbox.winfo_width() * 0.795, height=2, fg_color='gray25')
        MainWindowInstance.text_box._textbox.window_create("1.end", window=separator)
        MainWindowInstance.text_box.configure(state="disabled")

def add_text_to_textbox_slow(MainWindowInstance, text: str, delay=0.05):
    if text != "":
        MainWindowInstance.text_box.configure(state="normal")
        for char in text:
            MainWindowInstance.text_box.insert("end", char)
            MainWindowInstance.text_box.update_idletasks()
            time.sleep(delay)
        MainWindowInstance.text_box.insert("end", "\n")
        MainWindowInstance.text_box.configure(state="disabled")

def add_dict_to_textbox_slow(MainWindowInstance, in_dict: dict, delay=0.05):
    if in_dict:
        MainWindowInstance.text_box.configure(state="normal")
        for key, value in in_dict.items():
            line = f"{key}: {value}\n"
            for char in line:
                MainWindowInstance.text_box.insert("end", char)
                MainWindowInstance.text_box.update_idletasks()
                time.sleep(delay)
        MainWindowInstance.text_box.configure(state="disabled")

def add_dict_to_textbox(MainWindowInstance, in_dict: dict):
    if in_dict:
        MainWindowInstance.text_box.configure(state="normal")
        for key, value in in_dict.items():
            line = f"{key}: {value}\n"
            MainWindowInstance.text_box.insert("end", line)
        MainWindowInstance.text_box.configure(state="disabled")

def delete_all_entries(MainWindowInstance):
    MainWindowInstance.text_box.configure(state="normal")
    MainWindowInstance.text_box.delete("0.0", "end")
    MainWindowInstance.text_box.configure(state="disabled")

def add_choice_button(MainWindowInstance, text):
    choice_button = cTk.CTkButton(MainWindowInstance.choice_frame, text=text, command=lambda: MainWindowInstance.read_choice_buttons(choice=text))
    choice_button.pack(side="top", fill="x", padx=5, pady=5)

def delete_choice_buttons(MainWindowInstance):
    for widget in MainWindowInstance.choice_frame.winfo_children():
        widget.destroy()

def read_choice_buttons(MainWindowInstance, choice):
    MainWindowInstance.delete_choice_buttons()
    return choice

def gui_input(MainWindowInstance, gui_input_callback, label_text, y_position):
    input_label = cTk.CTkLabel(MainWindowInstance, text=label_text)
    input_label.place(relx=0.5, rely=y_position - 0.05, anchor="center")
    input_entry = cTk.CTkEntry(MainWindowInstance)
    input_entry.place(relx=0.5, rely=y_position, anchor="center")
    def handle_input(event):
        input_value = input_entry.get()
        input_entry.delete(0, "end")
        input_entry.destroy()
        input_label.destroy()
        gui_input_callback(MainWindowInstance, input_value)
    input_entry.bind("<Return>", handle_input)

def load_settings():
    from modules.game import Game
    global GUI_MODE
    try:
        with open("settings.txt", "r") as settings_file:
            settings_data = json.load(settings_file)
            GUI_MODE = settings_data.get("GUI_MODE", True)
            Game.sleep_time = settings_data.get("Game.sleep_time", 0.04)
            Game.separator_length = settings_data.get("Game.separator_length", 120)
    except FileNotFoundError:
        GUI_MODE = True
        Game.sleep_time = 0.04
        Game.separator_length = 120

def save_settings(gui_mode, sleep_time, separator_length):
    settings_data = {
        "GUI_MODE": gui_mode,
        "Game.sleep_time": sleep_time,
        "Game.separator_length": separator_length
    }
    with open("settings.txt", "w") as settings_file:
        json.dump(settings_data, settings_file)
    print("Settings saved!")
    close_settings_window()