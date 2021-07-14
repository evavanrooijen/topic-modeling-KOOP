from gensim.models import LdaModel

# load trained model from file
model =  LdaModel.load('lda_model')

for i in range(0, model.num_topics-1):
    print(f"Topic {i}")
    print(model.print_topic(i, topn = 3))

import pandas as pd
dtm = pd.read_csv("df_dtm.csv", index_col=0)
print(model.get_document_topics(dtm.iloc[10]))

# and another way, only prints top words
#for t in range(0, model.num_topics-1):
 #   print(f'topic {}: '.format(t) + ', '.join([v[1] for v in model.show_topic(t, 20)])
