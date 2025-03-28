# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/interaction.py
# Interacting with the GUI
# ====================================

import customtkinter as cTk
try:
    from design import MainWindow, InventoryWindow
except ModuleNotFoundError:
    from modules.gui.design import MainWindow, InventoryWindow

def confirm_player_name(StartWindowInstance, RUNNING_AS_MAIN):
    StartWindowInstance.player_name = StartWindowInstance.player_name_entry.get()
    if not RUNNING_AS_MAIN:
        if StartWindowInstance.player_name.strip() == "":
            StartWindowInstance.info_label.configure(text="Player name cannot be empty!")
        else:
            StartWindowInstance.info_label.configure(text=f"Player name confirmed: {StartWindowInstance.player_name}")
    else:
        StartWindowInstance.player_name = "<TESTING ENVIROMENT NOT MAIN.PY>"
        StartWindowInstance.info_label.configure(text="<TESTING ENVIROMENT NOT MAIN.PY> you can still start the game in this mode!")

def open_main_window(StartWindowInstance):
    if StartWindowInstance.player_name.strip() != "":
        StartWindowInstance.withdraw()
        MainWindow(StartWindowInstance, open_inventory, open_start_menu, add_text_to_textbox, resize_separators, delete_all_entries, print_latest_entry_from_textbox)
    else:
        StartWindowInstance.info_label.configure(text="Player name cannot be empty!")

def add_text_to_textbox(MainWindowInstance, text):
    if text != "":
        MainWindowInstance.text_box.configure(state="normal")
        MainWindowInstance.text_box.insert("1.0", text + "\n")
        separator = cTk.CTkFrame(MainWindowInstance.text_box, width=MainWindowInstance.text_box._textbox.winfo_width() * 0.795, height=2, fg_color='gray25')
        MainWindowInstance.text_box._textbox.window_create("1.end", window=separator)
        MainWindowInstance.text_box.configure(state="disabled")

def resize_separators(MainWindowInstance, event):
    MainWindowInstance.text_box.configure(state="normal")
    new_width = MainWindowInstance.text_box._textbox.winfo_width() * 0.795
    for child in MainWindowInstance.text_box.winfo_children():
        if isinstance(child, cTk.CTkFrame):
            child.configure(width=new_width)
    MainWindowInstance.text_box.configure(state="disabled")

def delete_all_entries(MainWindowInstance):
    MainWindowInstance.text_box.configure(state="normal")
    MainWindowInstance.text_box.delete("0.0", "end")
    MainWindowInstance.text_box.configure(state="disabled")

def print_latest_entry_from_textbox(MainWindowInstance):
    text = MainWindowInstance.text_box.get("1.0", "end-1c").split('\n')[0].strip()
    if text != "":
        print(f"Latest Entry: {text}")
    else:
        print("No entries available!")

def open_start_menu(MainWindowInstance):
    MainWindowInstance.master.deiconify()
    MainWindowInstance.destroy()

def open_inventory(MainWindowInstance):
    MainWindowInstance.withdraw()
    InventoryWindow(MainWindowInstance, close_inventory)

def close_inventory(InventoryWindowInstance):
    InventoryWindowInstance.master.deiconify()
    InventoryWindowInstance.destroy()
