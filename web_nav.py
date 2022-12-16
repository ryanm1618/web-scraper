from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import configparser
from bs4 import BeautifulSoup
from prod_info import prod_info
from selenium.webdriver.common.by import By
import time

class web_nav:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('/home/ryanmiller/Documents/Projects/PythonProjects/WebScraping/ebay_search/config.ini')

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')

        self.driver = webdriver.Chrome(self.config.get('Program', "config.driverpath"))

    def search_ebay(self, search_term):
        self.driver.get(self.config.get('Urls', "web.ebay"))
        self.driver.find_element(By.XPATH, self.config.get('XPath', 'ebay.searchinput')).send_keys(search_term)
        self.driver.find_element(By.XPATH, self.config.get('XPath', 'ebay.searchbutton')).click()

        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        info_list = []

        for product in soup.find_all('div', {'class' : "s-item__info clearfix"}):
            name = product.find('div', {'class' : "s-item__title"}).get_text()
            price = product.find('span', {'class' : "s-item__price"}).get_text()
    
            info_list.append(prod_info(name, price))

        return info_list
    #Going to be put on hold for now, I want to work up this idea with ebay to start since that 
    #works well enough.
    def search_mpb(self, search_term):
        self.driver.get(self.config.get('Urls', "web.mpb"))
        self.driver.find_element(By.XPATH, self.config.get('XPath', 'mpb.searchinput')).send_keys(search_term)
        self.driver.find_element(By.XPATH, self.config.get('XPath', 'mpb.searchinput')).send_keys(Keys.ENTER)
        time.sleep(5)

        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        result_list = []

        for product in soup.find_all('a', {'data-testid' : "model-card__cta"}):
            name = product.find('h4', {'data-testid' : "model-card__title"}).span.get_text()

            result_list.append(name)
        
        selected_result = self.select_result(result_list)

        elem_list = self.driver.find_elements(By.XPATH, "//a[@data-testid='model-card__cta']//span//h4//span")
        selected_elem = elem_list[int(selected_result)]
        selected_elem.click()

        #Now we can actually collect the search results
        #HOWEVER, it needs to be done with Selenium since Soup doesn't seem to want 
        #to work in this situation
        search_results = []
        result_containers = self.driver.find_elements(By.XPATH, "//div[@data-testid='search-results__grid-item']")

        for result in result_containers:
            #Heres the suspect, need to re-work this xpath 
            name = self.driver.find_element(By.XPATH, "//span[@data-testid='product-card__condition-description']").text
            price = self.driver.find_element(By.TAG_NAME, "//span[@data-testid='product-card__price']").text

            search_results.append(prod_info(name, price))
        
        return search_results
    
    def select_result(self, res_list):
        counter = 0
        for res in res_list:
            print(str(counter) + ". "+ res)
            counter += 1 
        
        choice = input("Enter the number of product to search: ")
        return choice

    def close(self):
        self.driver.quit()