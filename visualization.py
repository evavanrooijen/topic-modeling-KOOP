import streamlit as st
import pandas as pd

from gensim.models import LdaModel


st.title('Tekstuele Analyse - PLOOI Documenten')

st.sidebar.info("Dit is een visualisatie van de resultaten uit een NLP (Natural Language Processing) analyse van een set documenten uit PLOOI (solr testomgeving")

if st.sidebar.checkbox("Use default dataset", value = True) == False:
    fts = st.sidebar.selectbox("Select features", ("text", "ministerie", "tokenized_text"))
    n_docs = st.sidebar.slider("Select #documents", 0, 89300, 100)

## DATA COLLECTION - SOLR
dtm = pd.read_csv("df_dtm.csv", index_col=0)
df_tokenized = pd.read_csv("tokens.csv", index_col=0)

st.header(f' {dtm.shape[0]} documenten geanalyseerd')

selected_word = st.selectbox("Select word", dtm.columns)

st.text(f"Dit woord komt {dtm.loc[:, selected_word].sum()} vaak voor in deze set documenten en het meest in document")

#st.write(((dtm).head().sort_values(word, ascending=False))[['verantwoordelijke', word]])

#st.bar_chart(((dtm).head().sort_values(word, ascending=False))[[word]])

st.header("Most common words")
n_words = st.slider("Selecteer n (#woorden)", 1, 100, value=10)
#st.bar_chart(dtm.nlargest(n_words))

st.table(dtm.max(axis=0).sort_values(ascending=False)[:n_words])  

st.bar_chart(dtm.max(axis=0).sort_values(ascending=False)[:n_words])  

#st.table(dtm.max(axis=1)).sort_values(ascending=False)

st.text("To remove: numbers (maybe not 2025 -> toekomstvisie), ...")

selected_text = st.slider("Select a text", 0, dtm.shape[0])
st.bar_chart(dtm.iloc[selected_text].nlargest(n_words))
# show distribution words/doc
#st.bar_chart(df_tokenized.iloc[0].nlargest(10))

    #((df_tokenized[selected_text]).sort_values(word, ascending=False))[[word]])


if st.checkbox("Show text"):
    st.write(df_tokenized.text[selected_text])

st.header("Topic Modeling Results - Topic Dist per Text")
st.header("Word Distribution per Topic")

st.write(f"For same selected text as above #{selected_text}")
st.error("TO DO: IMPROVE")

st.header("Topic Modeling Results - Word Dist per Topic")

st.header("Word Distribution per Topic")
# load trained model from file
model =  LdaModel.load('lda_model')
selected_topic = st.slider("Select a topic index", 0, model.num_topics)
st.write(model.print_topic(selected_topic))
st.error("TO DO: IMPROVE")

if st.checkbox("Print all topics"):
    words_per_topic = st.slider("Print ... words per topic", 0, 20, 8)
    for i in range(0, model.num_topics-1):
        st.write(f"Topic {i}")
        st.write(model.print_topic(i, words_per_topic))




