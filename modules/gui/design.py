# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./modules/gui/design.py
# Design for the GUI
# ====================================

import customtkinter as cTk

class StartWindow(cTk.CTk):
    def __init__(self, open_main_window, confirm_player_name):
        super().__init__()
        self.player_name = ""
        self.title("The Flying Humpty - Main Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("720x320")

        self.player_name_entry = cTk.CTkEntry(self, placeholder_text="Enter your name")
        self.player_name_entry.place(relx=0.5, rely=0.5, anchor="center")

        self.confirm_player_name_btn = cTk.CTkButton(self, text="Confirm Name", command=lambda: confirm_player_name(self))
        self.confirm_player_name_btn.place(relx=0.5, rely=0.6, anchor="center")

        self.open_main_btn = cTk.CTkButton(self, text="Start", command=lambda: open_main_window(self))
        self.open_main_btn.place(relx=0.5, rely=0.7, anchor="center")

class MainWindow(cTk.CTkToplevel):
    def __init__(self, master, open_inventory, open_start_menu, add_text_to_textbox, resize_separators, delete_all_entries, print_latest_entry_from_textbox):
        super().__init__(master)
        self.title(f"{master.player_name}'s adventure among the Flying Humpty - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("1280x600")

        self.text_box = cTk.CTkTextbox(self)
        self.text_box.place(relx=0.05, rely=0.075, relwidth=0.9, relheight=0.45)
        self.text_box.configure(state="disabled")

        self.open_inventory_btn = cTk.CTkButton(self, text="Inventory", command=lambda: open_inventory(self))
        self.open_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        self.open_menu_btn = cTk.CTkButton(self, text="Menu", command=lambda: open_start_menu(self))
        self.open_menu_btn.place(relx=0.0, rely=0.0, anchor="nw", x=10, y=10)

        self.bind("<Configure>", lambda event: resize_separators(self, event))

        # TESTING

        self.TestingFrame = cTk.CTkFrame(self)
        self.TestingFrame.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.1)

        self.TestingEntry = cTk.CTkEntry(self.TestingFrame)
        self.TestingEntry.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        self.TestingButton = cTk.CTkButton(self.TestingFrame, text="Add Text Field", command=lambda: add_text_to_textbox(self))
        self.TestingButton.pack(side="right", padx=5, pady=5)

        self.TestingDeleteButton = cTk.CTkButton(self, text="Delete All Entries", command=lambda: delete_all_entries(self))
        self.TestingDeleteButton.place(relx=0.05, rely=0.7, relwidth=0.4, relheight=0.05)

        self.TestingPrintButton = cTk.CTkButton(self, text="Print Latest Entry", command=lambda: print_latest_entry_from_textbox(self))
        self.TestingPrintButton.place(relx=0.55, rely=0.7, relwidth=0.4, relheight=0.05)

class InventoryWindow(cTk.CTkToplevel):
    def __init__(self, master, close_inventory):
        super().__init__(master)
        self.player_name = master.player_name
        self.title(f"{self.player_name}'s Inventory - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("800x600")

        self.close_inventory_btn = cTk.CTkButton(self, text="Close", command=lambda: close_inventory(self))
        self.close_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

if __name__ == "__main__":
    from interactions import open_main_window, confirm_player_name
    root = StartWindow(open_main_window, confirm_player_name)
    root.mainloop()
