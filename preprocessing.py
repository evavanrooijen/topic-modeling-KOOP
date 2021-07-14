import pandas as pd

df = pd.read_json("outputfile.json")
df = df.dropna()
# get rid of lists for verantwoordelijke
df['verantwoordelijke'] = df['verantwoordelijke'].apply(lambda x: ','.join(map(str, x)))

print(f'Shape of df is {df.shape}')
#print(df.head())
# print distribution of topthemas
## TODO

from sklearn.feature_extraction.text import CountVectorizer
# initialize
cv = CountVectorizer(stop_words=['de', 'het', 'een', 'dat', 'en', 'in', 'is', 'van'], max_features=250) 

cv_matrix = cv.fit_transform(df['text']) 
# create document term matrix
df_dtm = pd.DataFrame(cv_matrix.toarray(), index=df.index, columns=cv.get_feature_names())
#print(df_dtm.head())

df_dtm.to_csv("df_dtm.csv")

# print number of unique values for ministeries
print(f'{df.verantwoordelijke.nunique()} unieke ministeries')

df_tokenized = df.join(df_dtm)

#print(df_tokenized.head())
df_tokenized.to_csv("tokens.csv")


print(f'{df_tokenized.verantwoordelijke.nunique()} unieke ministeries')
# join on index for merging with metadata and other feats
print(df_tokenized.groupby(['verantwoordelijke']).max())
df_tokenized.groupby(['verantwoordelijke']).mean().to_csv('grappig.csv')
## Leuk te combineren met geo locatie op visualisatie van woorden per plaats of per ministerie

print((df_tokenized).head().sort_values('één', ascending=False))

print(df_tokenized.columns)

