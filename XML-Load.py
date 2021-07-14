#Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
import pandas as pd

def loadRSS():
    # url of rss feed
    url = 'https://opendata.rijksoverheid.nl/v1/sources/rijksoverheid/infotypes/news'
	# creating HTTP response object from given url
    resp = requests.get(url)
    # saving the xml file
    with open('nieuwsberichten.xml', 'wb') as f:
        f.write(resp.content)

loadRSS()

xmlfile = 'nieuwsberichten.xml'
tree = ET.parse(xmlfile)

root = tree.getroot()

print(root)
print(root[0][1].text)
newsitems = []

for item in root.findall('./newsitem'):

        # empty news dictionary
        news = {}

        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            news[child.tag] = child.text.encode('utf8')
        # append news dictionary to news items list
        newsitems.append(news)
	

#df = pd.read_xml(xmlfile)

df = pd.DataFrame(newsitems)
df.to_csv('mooi.csv')


print(df.shape)

### voor elk bericht dataurl gebruiken voor inhoudelijke tekst
