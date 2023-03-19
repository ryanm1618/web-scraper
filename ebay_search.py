#from web_nav import web_nav
#from file_writer import file_writer
from curses_ui import curses_ui

#ebay_search = web_nav()
#search_item = input("Search ebay for: ")
#write_report = file_writer(ebay_search.search_ebay(search_item), 'Ebay')
#write_report.write_to_csv()

#Going to hold off on MPB for now due to the problems it's presenting.
#Definitely want to add this in the future
#write_report = file_writer(ebay_search.search_mpb(search_item), 'MPB')
#write_report.write_to_csv()
#ebay_search.close()

program = curses_ui()
program.run_gui()