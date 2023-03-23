from tkinter import *
from tkinter import ttk
import time

class t_gui:
    def __init__(self, config):
        self.config = config
        self.title = self.config.get('Program', 'program.title')
        self.version = self.config.get('Program', 'program.version')
        self.window = Tk()
        self.window.title(self.title)

        self.top_frame = Frame(self.window)
        self.top_menu_frame = Frame(self.top_frame)
        self.notebook_frame = Frame(self.top_frame)

        self.top_menu = Menu(self.top_menu_frame)
        self.file_menu = Menu(self.top_menu, tearoff=0)
        self.help_menu = Menu(self.top_menu, tearoff=0)
        self.notebook = ttk.Notebook(self.notebook_frame)
        self.home_tab_frame = Frame(self.notebook)

        self.window.config(menu=self.top_menu)

    def init_ui(self):
        self.notebook.add(self.home_tab_frame, text=self.config.get('UI', 'ui.hometabtitle'))


        #Packing time...
        self.top_menu_frame.pack()
        self.notebook_frame.pack()
        self.home_tab_frame.pack()
        
        self.notebook.pack()

    def t_main(self):
        self.window.mainloop()
        pass

