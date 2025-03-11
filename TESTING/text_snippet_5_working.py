import customtkinter as cTk

class MainWindow(cTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Text Snippet Test - Main Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("800x600")

        self.frame = cTk.CTkFrame(self)
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.45)
