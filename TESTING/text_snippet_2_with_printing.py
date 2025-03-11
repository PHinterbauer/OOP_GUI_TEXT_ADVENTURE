import customtkinter as ctk

class SnippetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Snippet Manager")

        self.snippets = []

        # Frame for snippets
        self.snippet_frame = ctk.CTkFrame(root)
        self.snippet_frame.pack(fill=ctk.BOTH, expand=True)

        # Canvas and scrollbar for snippets
        self.canvas = ctk.CTkCanvas(self.snippet_frame)
        self.scrollbar = ctk.CTkScrollbar(self.snippet_frame, orientation="vertical", command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Entry field for new snippet
        self.entry = ctk.CTkEntry(root, width=400)
        self.entry.pack(pady=10)

        # Button to add snippet
        self.add_button = ctk.CTkButton(root, text="Add Snippet", command=self.add_snippet)
        self.add_button.pack(pady=5)

        # Button to print latest snippet
        self.print_button = ctk.CTkButton(root, text="Print Latest Snippet", command=self.print_latest_snippet)
        self.print_button.pack(pady=5)

    def add_snippet(self):
        snippet_text = self.entry.get()
        if snippet_text:
            self.snippets.append(snippet_text)
            label = ctk.CTkLabel(self.scrollable_frame, text=snippet_text)
            label.pack(fill='x', expand=True, anchor="w", padx=10, pady=5)
            self.entry.delete(0, ctk.END)

    def print_latest_snippet(self):
        if self.snippets:
            print(self.snippets[-1])

if __name__ == "__main__":
    root = ctk.CTk()
    app = SnippetApp(root)
    root.mainloop()