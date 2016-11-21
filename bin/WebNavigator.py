from selenium import webdriver

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

## The Browser Class handles browsing the Web. __call__ returns the sourcecode
class Browser:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.driver = self.getDriver()

    def __call__(self, path=""):
        # Add the Optional Path to the BaseUrl
        url = urljoin(self.baseurl, path)
        # Load the site
        self.driver.get(url)
        # Return the SourceCode
        return self.driver.page_source

    def tearown(self):
        # Clean Up
        self.driver.close()

        if self.driver:
            print("\nCan't get rid of that shtty ErrorMsg:")
            self.driver.quit()

    def getByXpath(self, xPath):
        return self.driver.find_element_by_xpath(xPath)

    def getDriver(self):
        return webdriver.Chrome()

     def traverseTable(self, tableXpath, *classAttributes):
        tableBody = self.getByXpath(tableXpath)
        for row in tableBody.find_elements_by_xpath('.//tr'):
            dictator = {}
            for a in classAttributes:
                dictator.update({a: row.find_element_by_class_name(a)})
            yield (dictator)

class FirefoxBrowser(Browser):
    def getDriver(self):
        return webdriver.Firefox()
    
