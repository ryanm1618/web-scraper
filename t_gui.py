import tkinter as tk
from tkinter import ttk
import time

class t_gui(tk.Tk):
    def __init__(self, config):
        self.config = config
        self.title = self.config.get('Program', 'program.title')
        self.version = self.config.get('Program', 'program.version')
        self.window = tk.Tk()
        self.window.title(self.title + " v." + self.version)
        self.window.geometry(config.get('Program', 'program.windowsize'))
        ApplicationFrame(self.window).pack(side="top", fill="both", expand=True)

    def create_widgets(self):

        pass

    def t_main(self):
        self.init_ui()
        self.window.mainloop()

class ApplicationFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        pass
    
    def create_widgets(self):
        pass