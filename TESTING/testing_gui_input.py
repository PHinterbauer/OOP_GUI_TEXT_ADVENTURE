import customtkinter as cTk

def gui_input(MainWindowInstance, gui_input_callback, label_text, y_position):
    input_label = cTk.CTkLabel(MainWindowInstance, text=label_text)
    input_label.place(relx=0.5, rely=y_position - 0.05, anchor="center")
    input_entry = cTk.CTkEntry(MainWindowInstance)
    input_entry.place(relx=0.5, rely=y_position, anchor="center")
    def handle_input(event):
        input_value = input_entry.get()
        input_entry.delete(0, "end")
        input_entry.destroy()
        input_label.destroy()
        gui_input_callback(MainWindowInstance, input_value)
    input_entry.bind("<Return>", handle_input)

class TestWindow(cTk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Test Window")
        self.geometry("400x400")

        gui_input(self, self.process_integer_input, "SIGMA SIGMA LIGMA AN DER WAND (int):", 0.3)

        gui_input(self, self.process_string_input, "WER IST DER GOOFIESTE IM GANZEN LAND (str):", 0.6)

    def process_integer_input(self, MainWindowInstance, user_input):
        """Processes integer input."""
        try:
            user_choice = int(user_input)
            print(f"Integer input received: {user_choice}")
        except ValueError:
            print("Invalid input: Please enter a valid integer.")

    def process_string_input(self, MainWindowInstance, user_input):
        """Processes string input."""
        print(f"String input received: {str(user_input)}")

if __name__ == "__main__":
    test_window = TestWindow()
    test_window.mainloop()