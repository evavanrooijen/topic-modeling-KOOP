#Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
import pandas as pd
## url is item in list dataurl van 1.0


def loadRSS():
    # url of rss feed
    url = 'https://opendata.rijksoverheid.nl/v1/sources/rijksoverheid/infotypes/news/09313f0d-2a57-4e89-bdaf-458232fd8192'
	# creating HTTP response object from given url
    resp = requests.get(url)
    # saving the xml file
    with open('nieuwsbericht.xml', 'wb') as f:
        f.write(resp.content)

loadRSS()

xmlfile = 'nieuwsbericht.xml'
tree = ET.parse(xmlfile)

root = tree.getroot()

print(root)

newsitem = []

for item in root.findall('./document'):

        # empty news dictionary
        article = {}

        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            article[child.tag] = child.text.encode('utf8')
        # append news dictionary to news items list
        newsitem.append(article)
	

df = pd.DataFrame(newsitem)
df.to_csv('artikel2.csv')


print(df.shape)

### voor elk bericht dataurl gebruiken voor inhoudelijke tekst
