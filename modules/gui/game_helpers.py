# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/game_helpers.py
# Helper functions for the GUI in game
# ====================================

import customtkinter as cTk
import time

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
