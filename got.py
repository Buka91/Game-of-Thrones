# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

from urllib2 import urlopen

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'
response = urlopen(url).read()

soup = BeautifulSoup(response)

links = soup.findAll("a", attrs = {"href" : lambda L: L and L.startswith("/wiki/Game_of_Thrones_(season")})

viewersCounter = 0

alreadyUsed = list()
for link in links:
    if link.string[:6] == "Season" and link not in alreadyUsed:
        new_url = "https://en.wikipedia.org" + link["href"]
        season_response = urlopen(new_url).read()
        season_soup = BeautifulSoup(season_response)
        tables = season_soup.findAll("table", attrs = {"class": "wikitable plainrowheaders wikiepisodetable"})
        for table in tables:
            sup_list = table.findChildren("sup")
            for sup in sup_list:
                textNumber = sup.findParent("td").text
                viewersCounter += float(textNumber[:textNumber.find("[")])
        alreadyUsed.append(link)

print "Serijo si je skupaj ogledalo %s milijonov gledalcev." %viewersCounter