import requests
import os
import sys
import webbrowser
from lxml import html


print "******************************************************************"
print "**********                                              **********"
print "**********              SteamProfileInfo                **********"
print "**********             By Jordan Bottrell               **********"
print "**********                  4/28/2017                   **********"
print "**********                                              **********"
print "******************************************************************"
name = ''
while (name!= "quit"):
    name = raw_input("> Enter your Steam Profile URL (type 'quit' to exit)\n")
    if name == "quit":
        sys.exit()
    else:
        try:
            name_split = name.split("/")
            info = name_split[-1]
            baseURL = "http://steamidfinder.com/lookup/"
            fullURL = baseURL + info

            page = requests.get(fullURL)
            tree = html.fromstring(page.content)

#<div title="buyer-name">Carson Busses</div>
#<span class="item-price">$29.95</span>
#This will create a list of buyers:
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

            codeInfo = tree.xpath('//code/text()')

#codeInfo[4] is steamID 64
#codeInfo[6] is date created
#codeInfo[2] is steamID
#codeInfo[3] is steamID3
            print "\n\n"
            print "********************************"
            print "-----------USER INFO------------"
            print "********************************"
            print "Real name: " + codeInfo[8]
            print "Username: " + codeInfo[7]
            print "Date Created: " + codeInfo[6]
            print "SteamID: " + codeInfo[2]
            print "SteamID3: " + codeInfo[3]
            print "SteamID64: " + codeInfo[4]
            print "********************************"
            print "\n\n"
        except:
            print "\n\n"
            print "-----That is not a valid URL-----"
            print "\n\n"

sys.exit()
