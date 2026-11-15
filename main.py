import tkinter as tk
from tkinter import messagebox

class MirageStudyPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Mirage's Study Portal")
        self.root.geometry("500x400")
        
        label = tk.Label(root, text="Welcome to Mirage Study Portal!", font=("Arial", 14, "bold"))
        label.pack(pady=20)
        
        btn = tk.Button(root, text="Click Me", command=self.on_click)
        btn.pack(pady=10)

    def on_click(self):
        messagebox.showinfo("Status", "Study Portal is running successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MirageStudyPortal(root)
    root.mainloop()
