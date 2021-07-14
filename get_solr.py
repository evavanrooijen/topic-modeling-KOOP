import urllib.request
import json 
import pandas as pd

n_docs = 1600

#query = "http://solrcloud-lb-tst.overheid.nl:8983/solr/plooi/select?fl=text%2C%20topthema%2C%20verantwoordelijke&q=*%3A*&rows=4000&wt=json"

start = 0
rows = 50

df_docs = pd.DataFrame()

for i in range(n_docs):
    # build query for 100 docs
    query = f"http://solrcloud-lb-tst.overheid.nl:8983/solr/plooi/select?fl=text&q=*%3A*&rows={rows}&start={start}&wt=json"
    rows = rows + 50
    start = start + 50
    print(query)

    # get data from query
    connection = urllib.request.urlopen(query)
    response   = json.load(connection) 

    with open('outputfile.json', 'w') as fout:
        json.dump(response['response']['docs'], fout)
    new_rows = pd.read_json("outputfile.json")

    # append rows
    df_docs = df_docs.append(new_rows)

print(df_docs.head())
print(df_docs.shape)

print('aiming for 89359')

df_docs.to_csv('all_docs.csv')