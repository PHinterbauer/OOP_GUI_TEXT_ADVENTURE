# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/design.py
# Design for the GUI
# ====================================

import customtkinter as cTk
from PIL import Image

RUNNING_AS_MAIN = False

class StartWindow(cTk.CTk):
    def __init__(self, open_main_window, confirm_player_name, open_settings):
        super().__init__()

        self.player_name = ""
        self.title("The Flying Humpty - Main Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("720x320")

        pirate_ship_path = "./modules/gui/pictures/PIRATE_SHIP_REMOVEDBG.png"
        self.pirate_ship_image = cTk.CTkImage(light_image=Image.open(pirate_ship_path), dark_image=Image.open(pirate_ship_path), size=(200, 200))
        self.pirate_ship_label = cTk.CTkLabel(self, text="", image=self.pirate_ship_image)
        self.pirate_ship_label.place(relx=0.8, rely=0.5, anchor="center")

        hwi_logo_path = "./modules/gui/pictures/HWI_LOGO_REMOVEDBG.png"
        self.hwi_logo_image = cTk.CTkImage(light_image=Image.open(hwi_logo_path), dark_image=Image.open(hwi_logo_path), size=(200, 200))
        self.hwi_logo_label = cTk.CTkLabel(self, text="", image=self.hwi_logo_image)
        self.hwi_logo_label.place(relx=0.2, rely=0.5, anchor="center")

        self.player_name_entry = cTk.CTkEntry(self, placeholder_text="Enter your name")
        self.player_name_entry.place(relx=0.5, rely=0.5, anchor="center")

        self.info_label = cTk.CTkLabel(self, text="")
        self.info_label.place(relx=0.5, rely=0.4, anchor="center")

        self.confirm_player_name_btn = cTk.CTkButton(self, text="Confirm Name", command=lambda: confirm_player_name(self, RUNNING_AS_MAIN))
        self.confirm_player_name_btn.place(relx=0.5, rely=0.6, anchor="center")

        self.open_main_btn = cTk.CTkButton(self, text="Start", command=lambda: open_main_window(self))
        self.open_main_btn.place(relx=0.5, rely=0.7, anchor="center")

        self.open_settings_btn = cTk.CTkButton(self, text="Settings", command=lambda: open_settings(self))
        self.open_settings_btn.place(relx=0.5, rely=0.8, anchor="center")

class MainWindow(cTk.CTkToplevel):
    def __init__(self, master, open_inventory, open_start_menu, resize_separators):
        super().__init__(master)

        self.player_name = master.player_name
        self.title(f"{self.player_name}'s adventure among the Flying Humpty - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("1280x600")
        self.minsize(800, 500)

        self.text_box = cTk.CTkTextbox(self)
        self.text_box.place(relx=0.05, rely=0.075, relwidth=0.9, relheight=0.45)
        self.text_box.configure(state="disabled")

        self.open_inventory_btn = cTk.CTkButton(self, text="Inventory", command=lambda: open_inventory(self))
        self.open_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        self.open_menu_btn = cTk.CTkButton(self, text="Menu", command=lambda: open_start_menu(self))
        self.open_menu_btn.place(relx=0.0, rely=0.0, anchor="nw", x=10, y=10)

        self.choice_frame = cTk.CTkFrame(self)
        self.choice_frame.place(relx=0.05, rely=0.55, relwidth=0.45, relheight=0.25)
   
        self.bind("<Configure>", lambda event: resize_separators(self, event))

class InventoryWindow(cTk.CTkToplevel):
    def __init__(self, master, close_inventory):
        super().__init__(master)
        
        self.player_name = master.player_name
        self.title(f"{self.player_name}'s Inventory - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("800x600")

        self.close_inventory_btn = cTk.CTkButton(self, text="Close", command=lambda: close_inventory(self))
        self.close_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

class SettingsWindow(cTk.CTkToplevel):
    def __init__(self, master, save_settings, close_settings):
        super().__init__(master)

        self.player_name = master.player_name
        self.title(f"{self.player_name}'s Settings Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("700x400")

        self.gui_mode_label = cTk.CTkLabel(self, text="Enable GUI Mode:")
        self.gui_mode_label.place(relx=0.5, rely=0.1, anchor="center")

        self.gui_mode_switch = cTk.CTkSwitch(self, text="GUI Mode")
        self.gui_mode_switch.place(relx=0.5, rely=0.17, anchor="center")
        self.gui_mode_switch.toggle()

        self.sleep_time_label = cTk.CTkLabel(self, text="Game Sleep Time (float, default=0.04):")
        self.sleep_time_label.place(relx=0.5, rely=0.3, anchor="center")

        self.sleep_time_entry = cTk.CTkEntry(self)
        self.sleep_time_entry.place(relx=0.5, rely=0.37, anchor="center")
        self.sleep_time_entry.insert(0, "0.04")

        self.separator_length_label = cTk.CTkLabel(self, text="Separator Length (int, default=120):")
        self.separator_length_label.place(relx=0.5, rely=0.5, anchor="center")

        self.separator_length_entry = cTk.CTkEntry(self)
        self.separator_length_entry.place(relx=0.5, rely=0.57, anchor="center")
        self.separator_length_entry.insert(0, "120")

        self.save_button = cTk.CTkButton(self, text="Save Settings", command=lambda: self.save_and_close(save_settings=save_settings, close_settings=close_settings))
        self.save_button.place(relx=0.5, rely=0.7, anchor="center")

    def save_and_close(self, save_settings, close_settings):
        save_settings(self.gui_mode_switch, self.sleep_time_entry, self.separator_length_entry)
        close_settings()
        print("HALLO WELT!")

if __name__ == "__main__":
    from modules.gui.design_interactions import open_main_window, confirm_player_name
    RUNNING_AS_MAIN = True
    root = StartWindow(open_main_window, confirm_player_name)
    root.player_name = "<TESTING ENVIROMENT NOT MAIN.PY>"
    root.mainloop()
