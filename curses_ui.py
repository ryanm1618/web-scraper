import curses
import time

class curses_ui:
    def __init__(self):
        self.prog_title = "Price Mapper Version 0.0.0"
        self.item_str = "Item Selection"
        self.data_str = "Data Viewer"
        self.config_str = "Configuration"
        self.exit_str = "Exit"

    def c_main(self, stdscr):
        curses.curs_set(0)
        self.draw_main_menu(stdscr)
        
        
    def draw_main_menu(self, stdscr):
        max_y, max_x = stdscr.getmaxyx()
        mid_y = max_y//2
        mid_x = max_x//2 


        stdscr.addstr(mid_y - 2, )
        #text_y = max_y//2
        #text_x = max_x//2 - len(self.test_text)//2
        #stdscr.addstr(text_y, text_x, self.test_text)
        #stdscr.refresh()
        time.sleep(5)

    def run_gui(self):
        curses.wrapper(self.c_main)
    
