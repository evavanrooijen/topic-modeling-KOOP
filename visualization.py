import streamlit as st
import pandas as pd

st.title('Tekstuele Analyse - PLOOI Documenten')

st.sidebar.info("Dit is een visualisatie van de resultaten uit een NLP (Natural Language Processing) analyse van een set documenten uit PLOOI (solr testomgeving")

st.sidebar.selectbox("Select features", ("text", "ministerie"))
st.sidebar.slider("Select #documents", 0, 8000, 500)
st.sidebar.slider("Select range of docs", 0, 8000, 500)

## DATA COLLECTION - SOLR
dtm = pd.read_csv("df_dtm.csv", index_col=0)

st.header(f' {dtm.shape[0]} documenten geanalyseerd')

word = st.selectbox("Select word", dtm.columns)

st.write(((dtm).head().sort_values(word, ascending=False))[['verantwoordelijke', word]])

st.bar_chart(((dtm).head().sort_values(word, ascending=False))[[word]])

st.header("Most common words")
n_words = st.slider("Selecteer n (#woorden)", 1, 100, value=10)
#st.bar_chart(dtm.nlargest(n_words))

st.table(dtm.max(axis=0).sort_values(ascending=False)[:20])  

st.bar_chart(dtm.max(axis=0).sort_values(ascending=False)[:20])  

st.table(dtm.max(axis=1)).sort_values(ascending=False)

st.text("To remove: numbers (maybe not 2025 -> toekomstvisie), ...")

selected_text = st.slider("Select a text", 0, dtm.shape[0])
st.bar_chart(dtm.iloc[selected_text].nlargest(n_words))
# show distribution words/doc
#st.bar_chart(df_tokenized.iloc[0].nlargest(10))

    #((df_tokenized[selected_text]).sort_values(word, ascending=False))[[word]])


if st.checkbox("Show text"):
    st.write(df_tokenized.text[selected_text])

st.header("Topic Modeling Results - Topic Distribution for chosen text")

st.header("Word Distribution per Topic")
selected_topic = st.slider("Select a topic index", 0, 20)

st.error("TO DO")