# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/design.py
# Design for the GUI
# ====================================

import customtkinter as cTk
from PIL import Image, ImageSequence

class StartWindow(cTk.CTk):
    def __init__(self, open_main_window, confirm_player_name, open_settings):
        super().__init__()

        self.player_name = ""
        self.title("The Flying Humpty - Main Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("720x320")

        pirate_ship_path = "./resources/gifs/PIRATE_SHIP_GIF.gif"
        self.pirate_ship_frames = [cTk.CTkImage(light_image=frame.copy(), dark_image=frame.copy(), size=(200, 200)) for frame in ImageSequence.Iterator(Image.open(pirate_ship_path))]
        self.current_frame = 0
        self.pirate_ship_label = cTk.CTkLabel(self, text="", image=self.pirate_ship_frames[self.current_frame])
        self.pirate_ship_label.place(relx=0.8, rely=0.5, anchor="center")

        self.update_gif()

        hwi_logo_path = "./resources/images/HWI_LOGO_REMOVEDBG.png"
        self.hwi_logo_image = cTk.CTkImage(light_image=Image.open(hwi_logo_path), dark_image=Image.open(hwi_logo_path), size=(200, 200))
        self.hwi_logo_label = cTk.CTkLabel(self, text="", image=self.hwi_logo_image)
        self.hwi_logo_label.place(relx=0.2, rely=0.5, anchor="center")

        self.player_name_entry = cTk.CTkEntry(self, placeholder_text="Enter your name")
        self.player_name_entry.place(relx=0.5, rely=0.5, anchor="center")

        self.info_label = cTk.CTkLabel(self, text="")
        self.info_label.place(relx=0.5, rely=0.4, anchor="center")

        self.confirm_player_name_btn = cTk.CTkButton(self, text="Confirm Name", command=lambda: confirm_player_name(self))
        self.confirm_player_name_btn.place(relx=0.5, rely=0.6, anchor="center")

        self.open_main_btn = cTk.CTkButton(self, text="Start", command=lambda: open_main_window(self))
        self.open_main_btn.place(relx=0.5, rely=0.7, anchor="center")

        self.open_settings_btn = cTk.CTkButton(self, text="Settings", command=lambda: open_settings(self))
        self.open_settings_btn.place(relx=0.5, rely=0.8, anchor="center")

    def update_gif(self):
        self.current_frame = (self.current_frame + 1) % len(self.pirate_ship_frames)
        self.pirate_ship_label.configure(image=self.pirate_ship_frames[self.current_frame])
        self.after(100, self.update_gif)

class MainWindow(cTk.CTkToplevel):
    def __init__(self, master, open_inventory, open_start_menu):
        super().__init__(master)

        self.player_name = master.player_name
        self.title(f"{self.player_name}'s adventure among the Flying Humpty - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("1280x600")
        self.minsize(800, 500)
        self.input_callback_value = None

        self.text_box = cTk.CTkTextbox(self)
        self.text_box.place(relx=0.05, rely=0.1, relwidth=0.85, relheight=0.45)
        self.text_box.configure(state="disabled")

        self.open_inventory_btn = cTk.CTkButton(self, text="Inventory", command=lambda: open_inventory(self))
        self.open_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        self.open_menu_btn = cTk.CTkButton(self, text="Menu", command=lambda: open_start_menu(self))
        self.open_menu_btn.place(relx=0.0, rely=0.0, anchor="nw", x=10, y=10)

        self.choice_frame = cTk.CTkFrame(self)
        self.choice_frame.place(relx=0.05, rely=0.68, relwidth=0.45, relheight=0.3)

class InventoryWindow(cTk.CTkToplevel):
    def __init__(self, master, close_inventory):
        super().__init__(master)
        
        self.player_name = master.player_name
        self.title(f"{self.player_name}'s Inventory - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("800x600")

        self.close_inventory_btn = cTk.CTkButton(self, text="Close", command=lambda: close_inventory(self))
        self.close_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

class SettingsWindow(cTk.CTkToplevel):
    def __init__(self, master, save_and_close):
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

        self.save_button = cTk.CTkButton(self, text="Save Settings", command=lambda: save_and_close(self))
        self.save_button.place(relx=0.5, rely=0.7, anchor="center")
