import os

from selenium import webdriver
from bs4 import BeautifulSoup

class SeleniumConnection:
    browser = "webdriver.chrome.driver"

    def __init__(self, driverlocation, set_env=False):
        if set_env:
            os.environ[self.browser] = driverlocation

        self.driver = webdriver.Firefox()

    def __enter__(self):
        return self

    def __call__(self, url):
        self.driver.get(url)

        return self.driver.page_source

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print exc_type

        self.driver.quit()

class Soup:
    parser = "html.parser"
    def __init__(self, html):
        self._soup = BeautifulSoup(html, self.parser)

    def printout(self):
        print self._soup.prettify()
