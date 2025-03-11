import customtkinter as cTk

class main_window(cTk.CTk):
    def __init__(self):
        """
        Create the main window
        """
        super().__init__()

        self.title("Testing Window")
        self.geometry("400x500")

        # Create a frame to hold the text snippets
        self.text_frame = cTk.CTkFrame(self)
        self.text_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create a canvas to add a scrollbar
        self.canvas = cTk.CTkCanvas(self.text_frame)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add a scrollbar to the canvas
        self.scrollbar = cTk.CTkScrollbar(self.text_frame, orientation="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas to hold the text snippets
        self.snippet_frame = cTk.CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.snippet_frame, anchor="nw")

        # Initialize an empty list for text snippets
        self.text_snippets = []

        # Update the scroll region
        self.snippet_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Add an entry field for new text snippets
        self.new_snippet_entry = cTk.CTkEntry(self, placeholder_text="Enter new snippet")
        self.new_snippet_entry.pack(pady=10)

        # Add a button to add the new text snippet
        self.add_snippet_button = cTk.CTkButton(self, text="Add Snippet", command=self.add_snippet)
        self.add_snippet_button.pack(pady=10)

        # Add a button to print the latest text snippet
        self.print_button = cTk.CTkButton(self, text="Print Latest Snippet", command=self.print_latest_snippet)
        self.print_button.pack(pady=10)

        # Bind the configure event to update the snippet frame width
        self.bind("<Configure>", self.on_resize)

    def add_snippet(self):
        new_snippet = self.new_snippet_entry.get()
        if new_snippet:
            self.text_snippets.append(new_snippet)
            label = cTk.CTkLabel(self.snippet_frame, text=new_snippet, wraplength=self.snippet_frame.winfo_width(), anchor="w")
            label.pack(fill="x", pady=5)
            self.snippet_frame.update_idletasks()
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            self.new_snippet_entry.delete(0, 'end')

    def print_latest_snippet(self):
        if self.text_snippets:
            latest_snippet = self.text_snippets[-1]
            print(f"Latest Snippet: {latest_snippet}")
        else:
            print("No snippets available.")

    def on_resize(self, event):
        # Update the width of the snippet frame and its contents
        self.canvas.itemconfig(self.snippet_frame, width=event.width)
        for widget in self.snippet_frame.winfo_children():
            widget.configure(wraplength=event.width)

if __name__ == "__main__":
    root = main_window()
    root.mainloop()