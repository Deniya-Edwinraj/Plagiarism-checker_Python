import tkinter as tk
from gui import PlagiarismCheckerApp

if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    app = PlagiarismCheckerApp(root)  # Pass the root window to the app
    root.mainloop()  # Start the Tkinter event loop
