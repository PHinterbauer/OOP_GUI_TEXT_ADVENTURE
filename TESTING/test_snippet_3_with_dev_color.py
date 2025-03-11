import customtkinter as cTk

class MainWindow(cTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Text Snippet Test - Main Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("800x600")

        # Create a frame to hold the canvas and scrollbar
        frame = cTk.CTkFrame(self)
        frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.45)

        # Create a canvas
        self.canvas = cTk.CTkCanvas(frame, bg="red")
        self.canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Create a scrollbar
        scrollbar = cTk.CTkScrollbar(frame, command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y", padx=10, pady=10)

        # Configure the canvas to work with the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame to hold the button and entry field
        control_frame = cTk.CTkFrame(self)
        control_frame.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.1)

        # Create an entry field
        self.entry = cTk.CTkEntry(control_frame)
        self.entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

        # Create a button to add text fields to the canvas
        add_button = cTk.CTkButton(control_frame, text="Add Text Field", command=self.add_text_field)
        add_button.pack(side="right", padx=10, pady=10)

        # Create a frame inside the canvas to hold the text fields
        self.text_frame = cTk.CTkFrame(self.canvas, bg_color="blue")
        self.canvas.create_window((0, 0), window=self.text_frame, anchor="nw")

        # Configure the canvas to update the scroll region
        self.text_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Bind the canvas configure event to update the text field widths
        self.canvas.bind("<Configure>", self.update_text_field_widths)

    def add_text_field(self):
        text = self.entry.get()
        text_field = cTk.CTkLabel(self.text_frame, text=text, bg_color="grey")
        text_field.pack(fill="x", padx=5, pady=5, expand=True, anchor="w")
        self.update_text_field_widths()

    def update_text_field_widths(self, event=None):
        canvas_width = self.text_frame.winfo_width()
        for text_field in self.text_frame.winfo_children():
            text_field.configure(width=canvas_width)

if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()