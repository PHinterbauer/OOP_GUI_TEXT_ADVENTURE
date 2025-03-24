import customtkinter as cTk

class StartWindow(cTk.CTk):
    def __init__(self):
        """
        Create the start window
        """
        super().__init__()
        
        if __name__ != "__main__":
            self.player_name = ""
        else:
            self.player_name = "<TESTING ENVIROMENT NOT MAIN.PY>"

        self.title("The Flying Humpty - Main Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("720x320")

        self.player_name_entry = cTk.CTkEntry(self, placeholder_text="Enter your name")
        self.player_name_entry.place(relx=0.5, rely=0.5, anchor="center")

        self.confirm_player_name_btn = cTk.CTkButton(self, text="Confirm Name", command=self.confirm_player_name)
        self.confirm_player_name_btn.place(relx=0.5, rely=0.6, anchor="center")

        self.open_main_btn = cTk.CTkButton(self, text="Start", command=self.open_main_window)
        self.open_main_btn.place(relx=0.5, rely=0.7, anchor="center")

    def confirm_player_name(self,):
        self.player_name = self.player_name_entry.get()
        if __name__ != "__main__":
            if self.player_name.strip() == "":
                print("Player name cannot be empty!")
            else:
                print(f"Player name confirmed: {self.player_name}")
        else:
            self.player_name = "<TESTING ENVIROMENT NOT MAIN.PY>"

    def open_main_window(self):
        self.withdraw()
        MainWindow(self)

class MainWindow(cTk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title(f"{master.player_name}'s adventure among the Flying Humpty - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("1280x600")

        self.text_box = cTk.CTkTextbox(self)
        self.text_box.place(relx=0.05, rely=0.07, relwidth=0.9, relheight=0.45)
        self.text_box.configure(state="disabled")

        self.open_inventory_btn = cTk.CTkButton(self, text="Inventory", command=self.open_inventory)
        self.open_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        self.open_menu_btn = cTk.CTkButton(self, text="Menu", command=self.open_start_menu)
        self.open_menu_btn.place(relx=0.0, rely=0.0, anchor="nw", x=10, y=10)

        # TESTING
        self.TestingFrame = cTk.CTkFrame(self)
        self.TestingFrame.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.1)

        self.TestingEntry = cTk.CTkEntry(self.TestingFrame)
        self.TestingEntry.pack(side="left", fill="x", expand=True, padx=5, pady=5) 

        self.TestingButton = cTk.CTkButton(self.TestingFrame, text="Add Text Field", command=self.add_text_to_textbox)
        self.TestingButton.pack(side="right", padx=5, pady=5)

        self.TestingDeleteButton = cTk.CTkButton(self, text="Delete All Entries", command=self.delete_all_entries)
        self.TestingDeleteButton.place(relx=0.05, rely=0.7, relwidth=0.4, relheight=0.05)

        self.TestingPrintButton = cTk.CTkButton(self, text="Print Latest Entry", command=self.print_latest_entry_from_textbox)
        self.TestingPrintButton.place(relx=0.55, rely=0.7, relwidth=0.4, relheight=0.05)

    def add_text_to_textbox(self): # separator doesnt resize properly
        text = self.TestingEntry.get()
        if text != "":
            self.text_box.configure(state="normal")
            self.text_box.insert("1.0", text+"\n")
            separator = cTk.CTkFrame(self.text_box, width=self.text_box._textbox.winfo_width()-290, height=2, fg_color='gray25')
            self.text_box._textbox.window_create("1.end", window=separator)
            self.text_box.configure(state="disabled")

    def delete_all_entries(self):
        self.text_box.configure(state="normal")
        self.text_box.delete("0.0", "end")
        self.text_box.configure(state="disabled")

    def print_latest_entry_from_textbox(self):
        text = self.text_box.get("1.0", "end-1c").split('\n')[0].strip()
        if text != "":
            print(f"Latest Entry: {text}")
        else:
            print("No entries available!")

    def open_start_menu(self):
        self.master.deiconify()
        self.destroy()

    def open_inventory(self):
        self.withdraw()
        InventoryWindow(self)

class InventoryWindow(cTk.CTkToplevel):
    def __init__(self, master):
        """
        Create the inventory window
        """
        super().__init__(master)
        self.player_name = master.player_name

        self.title(f"{self.player_name}'s Inventory - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("800x600")

        self.close_inventory_btn = cTk.CTkButton(self, text="Close", command=self.close_inventory)
        self.close_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    def close_inventory(self):
        self.master.deiconify()
        self.destroy()

if __name__ == "__main__":
    root = StartWindow()
    root.mainloop()
