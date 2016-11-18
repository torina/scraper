from bs4 import BeautifulSoup
import WebNavigator
import MovieFabric

baseURL = "http://www.starz.com/movies"

pathTemplate = '//ul[@class="meta-list"]/li[{0}]'
titleXpath = '//div[@class="title"]/h1'
ratingxPath = pathTemplate.format(2)
timeXpath = pathTemplate.format(3)
genreXpath = pathTemplate.format(4)
yearXpath = pathTemplate.format(5)

browser = WebNavigator.Browser(baseURL)
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

    # caseCrew = browser.getByXpath('/h2[@class="slider-title"]')
    movie = factory.produceMovie(titleXpath, ratingxPath, timeXpath, genreXpath, yearXpath)
    print(str(movie))
browser.tearown()
