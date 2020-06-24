from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# class Kou_Tu:
#     def __init__(self):
#         self.driver = webdriver.Firefox()
#         self.url = 'https://magi.com/'
#
#     def get_content(self):
#         self.driver.get(self.url)
#         time.sleep(2)
#         self.driver.find_element_by_xpath("//input[@id='search-input']").send_keys("hh")
#         self.driver.find_element_by_xpath("//input[@id='search-submit']").click()
#
#     def __del__(self):
#         time.sleep(3)
#         self.driver.quit()
class Kou_Tu:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = 'https://www.remove.bg/'

    def get_content(self):
        self.driver.get(self.url)
        time.sleep(2)
        # self.driver.find_element_by_xpath("//input[@id='search-input']").send_keys("hh")
        self.driver.find_element_by_xpath("//a[@class='text-muted select-photo-url-btn']").click()

    def __del__(self):
        time.sleep(3)
        self.driver.quit()
if __name__ == '__main__':
    kou_tu = Kou_Tu()
    kou_tu.get_content()