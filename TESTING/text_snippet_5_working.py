import customtkinter as cTk

class MainWindow(cTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Text Snippet Test - Main Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("800x600")

        self.frame = cTk.CTkFrame(self)
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.45)

        self.canvas = cTk.CTkCanvas(self.frame, bg="grey", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.color_frame = cTk.CTkFrame(self.canvas, corner_radius=0)
        self.color_frame.pack(fill="both", expand=True)

        self.text_frame = cTk.CTkFrame(self.canvas, corner_radius=0)
        self.text_frame_id = self.canvas.create_window((0, 0), window=self.text_frame, anchor="nw")

        self.scrollbar = cTk.CTkScrollbar(self.frame, command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y", padx=5, pady=5)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.text_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", self.update_text_frame_width)

        # TESTING
        self.TestingFrame = cTk.CTkFrame(self)
        self.TestingFrame.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.1)

        self.TestingEntry = cTk.CTkEntry(self.TestingFrame)
        self.TestingEntry.pack(side="left", fill="x", expand=True, padx=5, pady=5) 

        self.TestingButton = cTk.CTkButton(self.TestingFrame, text="Add Text Field", command=self.add_text_field)
        self.TestingButton.pack(side="right", padx=5, pady=5)

        self.TestingDeleteButton = cTk.CTkButton(self, text="Delete All Entries", command=self.delete_all_entries)
        self.TestingDeleteButton.place(relx=0.05, rely=0.7, relwidth=0.4, relheight=0.05)

        self.TestingPrintButton = cTk.CTkButton(self, text="Print Latest Entry", command=self.print_latest_entry)
        self.TestingPrintButton.place(relx=0.55, rely=0.7, relwidth=0.4, relheight=0.05)

    def update_text_frame_width(self, event):
        canvas_width = self.canvas.winfo_width()
        scrollbar_width = self.scrollbar.winfo_width()
        self.canvas.itemconfigure(self.text_frame_id, width=canvas_width)
        for text_field in self.text_frame.winfo_children():
            if isinstance(text_field, cTk.CTkLabel):
                text_field.configure(wraplength=canvas_width - scrollbar_width - 200)

    def add_text_field(self):
        text = self.TestingEntry.get()
        if text != "":
            text_field = cTk.CTkLabel(self.text_frame, text=text, wraplength=self.canvas.winfo_width() - self.scrollbar.winfo_width() - 200)
            separator = cTk.CTkFrame(self.text_frame, height=2, bg_color="grey")
            text_field.pack(fill="x", padx=5, pady=5, expand=True, anchor="w")
            separator.pack(fill="x", anchor="w")
            if self.text_frame.winfo_children():
                first_child = self.text_frame.pack_slaves()[0]
                text_field.pack(fill="x", padx=5, pady=5, expand=True, anchor="w", before=first_child)
                separator.pack(fill="x", anchor="w", before=first_child)
            self.canvas.yview_moveto(0)

    def delete_all_entries(self):
        for widget in self.text_frame.winfo_children():
            widget.destroy()

    def print_latest_entry(self):
        if self.text_frame.winfo_children():
            for text_field in self.text_frame.pack_slaves():
                if isinstance(text_field, cTk.CTkLabel):
                    latest_text_field = text_field
                    break
            latest_entry = latest_text_field.cget("text")
            print(f"Latest Entry: {latest_entry}")
        else:
            print("No entries available!")

if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()        