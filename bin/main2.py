import sys
from openpyxl import Workbook
from openpyxl.compat import range
import WebNavigator
import ChannelLineup

# configs
baseURLWow = "http://www.wowway.com/support/tv/channel-lineups"
LOCATION_XPATH = '//*[@id="location-gate"]/div[2]/ul/li[{0}]/a'
locationAgrument = str(sys.argv[1])
destination = locationAgrument.lower().title()
if destination == 'Auburn':
    print("AUBURN selected")
    LOCATION = LOCATION_XPATH.format(1)
    MARKET_AMOUNT = 13
elif locationAgrument == 'Chicago':
    print("CHICAGO selected")
    LOCATION = LOCATION_XPATH.format(4)
    MARKET_AMOUNT = 6
else:
    print("Please, input location. Available values: AUBURN, CHICAGO")
    quit()

MARKET_PATH = '//*[@id="SelectedRegionId"]/option[{0}]'

# excel setup
wb = Workbook()
destFile = "Wow-{}.xlsx".format(destination)

browser = WebNavigator.Browser(baseURLWow)
html = browser()
locationElem = browser.getByXpath(LOCATION)
locationElem.click()

for i in range(2, MARKET_AMOUNT + 2):
    market = browser.getByXpath(MARKET_PATH.format(i))
    print(market.text)
    if i == 2:
        marketSheet = wb.active
        marketSheet.title = market.text
    else:
        marketSheet = wb.create_sheet(market.text)
    market.click()

    #title row
    marketSheet.append(["Network", "Channel", "HD Channel", "Small Cable\n (Previously limited)",
                        "Medium Cable\n (PREVIOUSLY BASIC)", "Large Cable\n (Previously Limited)"])

    tableXpath = '//*[@id="table-channel-lineup"]/div[2]/table/tbody'
    classAttrs = ['network', 'channel', 'channel-hd', 'pkg1', 'pkg2', 'pkg3']

    for d in browser.traverseTable(tableXpath, *classAttrs):
        print(d)
        
    marketSheet.append([channelLineUp.network, channelLineUp.channel, channelLineUp.hd, channelLineUp.small,
                            channelLineUp.medium, channelLineUp.large])

wb.save(filename=destFile)
browser.tearown()
