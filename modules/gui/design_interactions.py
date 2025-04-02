# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/interaction.py
# Interacting with the GUI
# ====================================

import customtkinter as cTk
from PIL import Image
from modules.game import Game
try:
    from design import MainWindow, InventoryWindow
except ModuleNotFoundError:
    from modules.gui.design import MainWindow, InventoryWindow

SettingsWindowInstance = None

def open_settings(parent):
    global SettingsWindowInstance
    if SettingsWindowInstance is None or not SettingsWindowInstance.winfo_exists():
        from modules.gui.design import SettingsMenu
        SettingsWindowInstance = SettingsMenu(parent)
        SettingsWindowInstance.grab_set()
    else:
        SettingsWindowInstance.focus()

def close_settings():
    global SettingsWindowInstance
    if SettingsWindowInstance is not None and SettingsWindowInstance.winfo_exists():
        SettingsWindowInstance.destroy()
        SettingsWindowInstance = None

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

def resize_separators(MainWindowInstance, event):
    MainWindowInstance.text_box.configure(state="normal")
    new_width = MainWindowInstance.text_box._textbox.winfo_width() * 0.795
    for child in MainWindowInstance.text_box.winfo_children():
        if isinstance(child, cTk.CTkFrame):
            child.configure(width=new_width)
    MainWindowInstance.text_box.configure(state="disabled")

def open_main_window(StartWindowInstance):
    if StartWindowInstance.player_name.strip() != "":
        StartWindowInstance.withdraw()
        Game.MainWindowInstance = MainWindow(StartWindowInstance, open_inventory, open_start_menu, resize_separators)
    else:
        StartWindowInstance.info_label.configure(text="Player name cannot be empty!")

def open_start_menu(MainWindowInstance):
    MainWindowInstance.master.deiconify()
    MainWindowInstance.destroy()

def open_inventory(MainWindowInstance):
    MainWindowInstance.withdraw()
    InventoryWindow(MainWindowInstance, close_inventory)

def close_inventory(InventoryWindowInstance):
    InventoryWindowInstance.master.deiconify()
    InventoryWindowInstance.destroy()
