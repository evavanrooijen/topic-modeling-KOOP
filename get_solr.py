import urllib.request
import json 
import pandas as pd

query = "http://solrcloud-lb-tst.overheid.nl:8983/solr/plooi/select?fl=text%2C%20topthema%2C%20verantwoordelijke&q=*%3A*&rows=4000&wt=json"

connection = urllib.request.urlopen(query)
response   = json.load(connection) 

with open('outputfile.json', 'w') as fout:
    json.dump(response['response']['docs'], fout)
