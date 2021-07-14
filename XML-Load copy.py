#Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
import pandas as pd

xmlfile = 'nieuwsbericht.xml'
tree = ET.parse(xmlfile)

root = tree.getroot()

items = []

for item in root.findall('./document'):

        # empty news dictionary
        news = {}

        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            news[child.tag] = child.text.encode('utf8')
        # append news dictionary to news items list
        items.append(news)

df = pd.DataFrame(items)
df.to_csv('mooi 2.0.csv')

print(df.shape)

### voor elk bericht dataurl gebruiken voor inhoudelijke tekst
