
from selenium import webdriver
from bs4 import BeautifulSoup

# Same as urllib.parse
from urlparse import urljoin

## The Browser Class handles browsing the Web. __call__ returns the sourcecode
class Browser:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.driver = webdriver.Firefox()

    def __call__(self, path=""):
        # Add the Optional Path to the BaseUrl
        url = urljoin(self.baseurl, path)
        # Load the site
        self.driver.get(url)
        # Return the SourceCode
        return self.driver.page_source

    def teardown(self):
        # Clean Up
        self.driver.close()

        if self.driver:
            print "\nCan't get rid of that shtty ErrorMsg:"
            self.driver.quit()

## Soup Class is a Wrapper around BeautifulSoup. Basically parses the provied Html
class Soup:
    parser = "html.parser"

    def __init__(self, html):
        self._soup = BeautifulSoup(html, self.parser)

    def findByConfig(self, config, expectone=True):
        result = self._soup.find_all(**config)

        if not expectone:
            return result

        if len(result) != 1:
            print result
            return None

        return result[0]

    def printout(self):
        print self._soup.prettify()

## UrlProvider extracts the urls from a sourcehtml according to Configuration
class UrlProvider:
    def __init__(self, sourcehtml, config, urlkey):
        soup = Soup(sourcehtml)

        self.urlkey = urlkey
        self.urls = soup.findByConfig(config, expectone=False)

    def Next(self):
        for i, url in enumerate(self.urls):

            yield i, url[self.urlkey]

## MovieFabric produces the Class Movie according to config
class MovieFabric:
    def __init__(self, *extractionConfigs):
        self.exconfigs = extractionConfigs

    def __call__(self, html):
        soup = Soup(html)

        movieargs = []
        for config in self.exconfigs:
            movieargs.append(soup.findByConfig(config))

        return Movie(*movieargs)

## Class Movie is the result class. use str(movie) for nice string representation
class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        if not self.name or not self.rating:
            return "ERROR WITH MOVIE"

        return "Name: " + self.name.text + " -- Rating: " + self.rating.text

## Scraper Class scraps Website according to config
class Scraper:
    def __init__(self, config):
        self.browser = Browser(config.BaseUrl)

        self.urlprovider = UrlProvider(self.browser(), config.MovieConfig, config.UrlKey)

        self.fabric = MovieFabric(config.TitleConfig, config.RatingConfig)

        self.killswitch = config.KillSwitch

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.teardown()

    def Next(self):

        for i, url in self.urlprovider.Next():

            if self.killswitch and i >= self.killswitch:
                return

            html = self.browser(url)

            model = self.fabric(html)

            yield model
