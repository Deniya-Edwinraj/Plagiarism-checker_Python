import tkinter as tk
from tkinter import filedialog, messagebox, font
from plagiarism_checker import read_file_with_textract, check_plagiarism

class PlagiarismCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Checker")
        self.root.geometry("400x300")  # Set a fixed size for the window
        self.root.config(bg="#f0f0f0")  # Light grey background
        self.text1_path = ""
        self.text2_path = ""

        # Frame for content
        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(pady=20)

        # Title Label
        self.title_label = tk.Label(
            self.frame, 
            text="Plagiarism Checker", 
            font=("Helvetica", 16, "bold"), 
            bg="#f0f0f0"
        )
        self.title_label.pack(pady=10)

        # File selection buttons
        self.select_file1_btn = tk.Button(
            self.frame, 
            text="Select File 1", 
            command=self.select_file1,
            bg="#007BFF", 
            fg="white", 
            font=("Helvetica", 12),
            relief=tk.FLAT
        )
        self.select_file1_btn.pack(pady=10, padx=20, fill=tk.X)

        self.select_file2_btn = tk.Button(
            self.frame, 
            text="Select File 2", 
            command=self.select_file2,
            bg="#007BFF", 
            fg="white", 
            font=("Helvetica", 12),
            relief=tk.FLAT
        )
        self.select_file2_btn.pack(pady=10, padx=20, fill=tk.X)

        self.check_btn = tk.Button(
            self.frame, 
            text="Check Plagiarism", 
            command=self.check_plagiarism,
            bg="#28A745", 
            fg="white", 
            font=("Helvetica", 12),
            relief=tk.FLAT
        )
        self.check_btn.pack(pady=20, padx=20, fill=tk.X)

        self.result_label = tk.Label(
            self.frame, 
            text="", 
            bg="#f0f0f0", 
            font=("Helvetica", 12, "italic")
        )
        self.result_label.pack(pady=10)

    def select_file1(self):
        self.text1_path = filedialog.askopenfilename(title="Select File 1", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    def select_file2(self):
        self.text2_path = filedialog.askopenfilename(title="Select File 2", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    def check_plagiarism(self):
        if not self.text1_path or not self.text2_path:
            messagebox.showwarning("Warning", "Please select two text files.")
            return

        try:
            text1 = read_file_with_textract(self.text1_path)
            text2 = read_file_with_textract(self.text2_path)

            if text1 is None or text2 is None:
                messagebox.showerror("Error", "Failed to read one or both files.")
                return

            similarity = check_plagiarism(text1, text2)
            self.result_label.config(text=f"Similarity: {similarity:.2f}%", fg="#28A745")  # Change text color to green
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlagiarismCheckerApp(root)
    root.mainloop()
