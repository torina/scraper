
from selenium import webdriver
from bs4 import BeautifulSoup

# Same as urllib.parse
from urlparse import urljoin

HEADERCONFIG = {"name": "div", "class_": "title"}
TITLECONFIG = {"name": "h1"}
RATINGCONFIG = {"name": "li", "attrs": {"ng-if": "vm.details.mpaaRating"} }

class Browser:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.driver = webdriver.Firefox()

    def __call__(self, path=""):

        url = urljoin(self.baseurl, path)

        self.driver.get(url)

        return self.driver.page_source

    def teardown(self):
        self.driver.close()

        if self.driver:
            print "\nCan't get rid of that shtty ErrorMsg:"
            self.driver.quit()

class Soup:
    parser = "html.parser"
    def __init__(self, html):
        self._soup = BeautifulSoup(html, self.parser)

    def loopMovieUrl(self):
        for mvslice in self._soup.find_all("a", class_="slick-link"):
            yield self.getMovieUrl(mvslice)

    def getMovieUrl(self, mvslice):
        return mvslice['href']

    def findOneByConfig(self, config, soup=None):
        if not soup:
            soup = self._soup

        result = self._soup.find_all(**config)

        if len(result) != 1:
            print result
            return None

        return result[0]

    def findTitle(self):
        header = self.findOneByConfig(HEADERCONFIG)

        return self.findOneByConfig(TITLECONFIG, soup=header)

    def findRating(self):
        return self.findOneByConfig(RATINGCONFIG)

    def printout(self):
        print self._soup.prettify()

class Movie:
    def __init__(self, moviesoup):
        self.name = moviesoup.findTitle()
        self.rating = moviesoup.findRating()

    def __str__(self):
        if not self.name or not self.rating:
            return "ERROR WITH MOVIE"

        return "Name: " + self.name.text + " -- Rating: " + self.rating.text

class Scraper:
    def __init__(self, sourceurl):
        self.browser = Browser(sourceurl)

        self.mainpage = Soup(self.browser())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.teardown()

    def browsePage(self, killswitch=None):
        for i, movieurl in enumerate(self.mainpage.loopMovieUrl()):

            if killswitch and i >= killswitch:
                return

            html = self.browser(movieurl)

            moviepage = Soup(html)

            movie = Movie(moviepage)

            yield movie
