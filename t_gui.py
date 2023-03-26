from tkinter import *
from tkinter import ttk
import time

class t_gui:
    def __init__(self, config):
        self.config = config
        self.title = self.config.get('Program', 'program.title')
        self.version = self.config.get('Program', 'program.version')
        self.window = Tk()
        self.window.title(self.title + " v." + self.version)
        self.window.geometry(config.get('Program', 'program.windowsize'))

        self.top_menu = Menu(self.window)
        self.file_menu = Menu(self.top_menu)
        self.help_menu = Menu(self.top_menu)
        self.notebook = ttk.Notebook(self.window)
        self.home_tab_frame = Frame(self.notebook)

        self.window.config(menu=self.top_menu)

    def init_ui(self):

        self.notebook.add(self.home_tab_frame, text=self.config.get('UI', 'ui.hometabtitle'))
        self.notebook.place(x=0, y=20)


        

    def t_main(self):
        self.init_ui()
        self.window.mainloop()
        pass

