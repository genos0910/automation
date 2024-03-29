from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class GoogleSearchPage:
    URL = 'https://www.google.com'

    SEARCH_BOX = (By.NAME, 'q')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_BOX)
        search_input.send_keys(phrase + Keys.RETURN)
