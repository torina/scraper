import scraper as scr

WEBPAGEURL = "http://www.starz.com/movies/26915"
DRIVERLOCATION = "/Users/Kokweazel/scraper/chromedriver"

# print con.__dict__

if __name__ == '__main__':
    with scr.SeleniumConnection(DRIVERLOCATION) as connection:

        html = connection(WEBPAGEURL)

        soup = scr.Soup(html)

        soup.printout()





## REFERENCE CODE ##

# driver = webdriver.Chrome()
# driver.get(wiki)

# req = urllib2.Request(wiki)
# response = urllib2.urlopen(req)
# html = response.read()

# print 'Set 30 years after Return' in str(html)

# soup = BeautifulSoup(str(html), "html.parser")
# soup = soup.prettify()
# print 'Set 30 years after Return' in soup
# lobbying = {}

# print soup.find_all("a", class_="slick-link")

# for mvSlice in soup.find_all("a", class_="slick-link"):
#     href = (mvSlice['href'])
#     print wiki, href
    # movieUrl = urljoin(wiki, href)
#     driver.get(movieUrl)
#     html = driver.page_source
#     soup = BeautifulSoup(html, "html.parser")
#     pretty = soup.prettify()

# title = soup.find_all(True)
# for tag in title:
#     if tag.has_attr('data-ng-controller'):
#         break

# section = tag.find_all("section")[0]

# subsection = section.find_all("div")[0]

# print soup.prettify()

# #     #print(title.find_all("h1")[0].text)
# #     lobbying[title.find_all("h1")[0].text] = {} #create new dict

# # print soup.find_all("section", class_="block-details")

# rating = soup.find_all("li", {"ng-if": "vm.details.mpaaRating"})
# print rating
#     #print(rating[0].text)
#     # error here
#     if(rating[0] != None):
#         lobbying[title.find_all("h1")[0].text]["rate"] = rating[0].text

# for item in lobbying.keys():
#     print(item + ": " + "\n\t" + "rate: " + lobbying[item]["rate"] + "\n\n")
