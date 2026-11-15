import tkinter as tk

class StudyPortalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mirage Study Portal")
        self.geometry("600x450")
        
        # Main container that holds all pages
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        # Register all application pages
        for PageClass in (HomePage, StudyNotesPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            # Stack frames on top of each other in the same grid cell
            frame.grid(row=0, column=0, sticky="nsew")
            
        # Show the home page by default
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """Bring the chosen page frame to the front"""
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = tk.Label(self, text="Welcome to Study Portal Dashboard", font=("Arial", 16, "bold"))
        label.pack(pady=40)
        
        # Navigation Button to go to Study Notes
        btn_notes = tk.Button(
            self, 
            text="Open Study Notes", 
            font=("Arial", 12),
            command=lambda: controller.show_frame("StudyNotesPage")
        )
        btn_notes.pack(pady=10)

class StudyNotesPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = tk.Label(self, text="Your Study Notes", font=("Arial", 16, "bold"))
        label.pack(pady=30)
        
        notes_content = tk.Label(
            self, 
            text="• Python Networking & Sockets\n• Computer Systems & Architecture\n• Tkinter GUI Layouts", 
            font=("Arial", 11),
            justify="left"
        )
        notes_content.pack(pady=10)
        
        # Navigation Button to go back Home
        btn_home = tk.Button(
            self, 
            text="Back to Home", 
            font=("Arial", 12),
            command=lambda: controller.show_frame("HomePage")
        )
        btn_home.pack(pady=20)

if __name__ == "__main__":
    app = StudyPortalApp()
    app.mainloop()
