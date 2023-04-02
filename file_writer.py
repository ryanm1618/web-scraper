import csv
from prod_info import prod_info
from datetime import datetime

class FileWriter:

    def __init__(self, info_list, site_name):
        self.ilist = info_list
        self.name = site_name

    def write_to_csv(self):
        time = datetime.now()
        file_name = self.name + time.strftime("%m%d%Y.%H.%M.%S")
        file = open('./csv/' + file_name + '.csv', 'w')
        writer = csv.writer(file)
        for item in self.ilist:
            row = [item.get_name(), item.get_price()]
            writer.writerow(row)
        
        file.close()