import pandas as pd

df = pd.read_csv("all_docs.csv")

# drop NA and/or duplicates
df = df.dropna()
df = df.drop_duplicates()
print(f"Number of duplicates: {df.duplicated().sum()} and number NaN: {df.text.isna().sum()}")

# get rid of lists for verantwoordelijke
#df['verantwoordelijke'] = df['verantwoordelijke'].apply(lambda x: ','.join(map(str, x)))

print(f'Shape of df is {df.shape}')

# print distribution of topthemas
## TODO

from sklearn.feature_extraction.text import CountVectorizer
# initialize
df_stop = pd.read_json('stop.json')
stop = list(df_stop.iloc[:][0])

for i in range(1500):
    stop.append(str(i))


cv = CountVectorizer(stop_words=stop, max_features=250) 

cv_matrix = cv.fit_transform(df['text']) 
# create document term matrix
df_dtm = pd.DataFrame(cv_matrix.toarray(), index=df.index, columns=cv.get_feature_names())
#print(df_dtm.head())

df_dtm.to_csv("df_dtm.csv")

# print number of unique values for ministeries
#print(f'{df.verantwoordelijke.nunique()} unieke ministeries')

df_tokenized = df.join(df_dtm)

#print(df_tokenized.head())
df_tokenized.to_csv("tokens.csv")

#print(f'{df_tokenized.verantwoordelijke.nunique()} unieke ministeries')
# join on index for merging with metadata and other feats
#print(df_tokenized.groupby(['verantwoordelijke']).max())
#df_tokenized.groupby(['verantwoordelijke']).mean().to_csv('grappig.csv')
## Leuk te combineren met geo locatie op visualisatie van woorden per plaats of per ministerie

#print((df_tokenized).head().sort_values('één', ascending=False))

print(df_tokenized.columns[:30])

print("most common words")

n_words = 20
print(df_dtm.max(axis=0).sort_values(ascending=False)[:n_words].index)