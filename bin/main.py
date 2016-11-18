from bs4 import BeautifulSoup
import WebNavigator
import MovieFabric
# configs
# http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement
baseURL = "http://www.starz.com/movies"

#setting XPathes for every elem.
titleXpath = '//div[@class="title"]/h1'

pathTemplate = '//ul[@class="meta-list"]/li[{0}]'
ratingxPath = pathTemplate.format(2)
timeXpath = pathTemplate.format(3)
genreXpath = pathTemplate.format(4)
yearXpath = pathTemplate.format(5)
castCrew = '//div[@class="block-description"]'

# end config
browser = WebNavigator.FirefoxBrowser(baseURL)
html = browser()

soup = BeautifulSoup(html, "html.parser")
results = {}

factory = MovieFabric.MovieFabric(browser)
# for [presumably] all hrefs
for mvSlice in soup.find_all("a", class_="slick-link"):
    href = (mvSlice['href'])
    # todo how to move through pages
    movieHtml = browser(href)
    soup = BeautifulSoup(movieHtml, "html.parser")
    pretty = soup.prettify()


    movie = factory.produceMovie(titleXpath, ratingxPath, timeXpath, genreXpath, yearXpath, castCrew)
    print(str(movie))
browser.tearown()
