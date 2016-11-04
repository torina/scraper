from urllib.parse import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import os

chromedriver = "C:/Program Files/chrome/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
#todo remove

wiki = "http://www.starz.com/movies"
driver.get(wiki)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

for mvSlice in soup.find_all("a", class_="slick-link"):
    href = (mvSlice['href'])
    movieUrl = urljoin(wiki, href)
    print(movieUrl)
    driver.get(movieUrl)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    pretty = soup.prettify()

    title = soup.find_all("div", class_="title")[0]
    print(title.find_all("h1")[0].text)

#make a wrapper
    rating = soup.find_all("li", {"ng-if": "vm.details.mpaaRating"})
    print(rating[0].text)

driver.quit()
