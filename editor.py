import json
from tkinter import Tk, Text, Menu, filedialog, messagebox

# Load settings
def load_settings():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Default settings if config.json doesn't exist
        return {
            "font_size": 12,
            "theme": "light",
            "font_family": "Courier",
            "default_file_path": ""
        }

# Save settings
def save_settings(settings):
    with open("config.json", "w") as file:
        json.dump(settings, file, indent=4)

# Main editor class
class CodeEditor:
    def __init__(self, root, settings):
        self.root = root
        self.settings = settings

        # Configure the editor window
        self.root.title("Code Editor")
        self.text_area = Text(root, font=(settings["font_family"], settings["font_size"]))
        self.text_area.pack(expand=True, fill="both")

        # Menu bar
        self.menu = Menu(root)
        root.config(menu=self.menu)

        # File menu
        file_menu = Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Settings", command=self.open_settings)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        self.menu.add_cascade(label="File", menu=file_menu)

    def open_file(self):
        file_path = filedialog.askopenfilename(initialdir=self.settings["default_file_path"])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", "end-1c"))

    def open_settings(self):
        # Create a simple settings dialog (not implemented here for brevity)
        messagebox.showinfo("Settings", "Open the settings dialog here.")

# Initialize the app
if __name__ == "__main__":
    root = Tk()
    settings = load_settings()
    app = CodeEditor(root, settings)
    root.mainloop()

    # Save settings on exit
    save_settings(settings)
