from tkinter import *
from tkinter import ttk
import time

class t_gui:
    def __init__(self, config):
        self.config = config
        self.title = config.get('Program', 'program.title')
        self.version = config.get('Program', 'program.version')
        self.window = Tk()
        self.window.title(self.title)

    def t_main(self):
        self.window.mainloop()
        pass

