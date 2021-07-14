import pandas as pd
import numpy as np

df_tokenized = pd.read_csv("tokens.csv")

#print(pd.histogram(df_tokenized.iloc[0]))
#print(df_tokenized.dtypes)

#print(df_tokenized.belang.nlargest(10))
#print(df_tokenized.iloc[0].sort_values(ascending=False))
series = df_tokenized.iloc[0]
print(type(series))
#print(series.idxmax())

dtm = pd.read_csv("df_dtm.csv")
#print(dtm.knooppunt.sort_values())
#print(dtm.head())
#print(df_tokenized.text[24])

#print(dtm.loc[:, 'zowel'].sum())
dtm.max(axis=0).sort_values(ascending=False).to_csv('most_common.csv')
(list(dtm.max(axis=0).sort_values(ascending=False).index.values))

np.savetxt("check.csv", 
           list(dtm.max(axis=0).sort_values(ascending=False).index.values),
           delimiter =", ", 
           fmt ='% s')

