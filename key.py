from keyphrase_vectorizers import KeyphraseCountVectorizer
import streamlit as st
from transformers import pipeline


docs = []

keyphrases_output = []
val = 0
# Init default vectorizer.
def vectorize(tex):
    docs = []
    docs.append(tex)
    val = 1
    vectorizer = KeyphraseCountVectorizer()
    document_keyphrase_matrix = vectorizer.fit_transform(docs).toarray()
    global keyphrases_output
    print(vectorizer.get_params())
    if(len(keyphrases_output) == 0):
        keyphrases = list(vectorizer.get_feature_names_out())
        for i in keyphrases:
            keyphrases_output.append(i)
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        st.header("Summary Of Text")
        st.text(summarizer(docs, max_length=130, min_length=30, do_sample=False)[0]["summary_text"])
        st.header("Keywords from Audio: ")
        st.json(keyphrases_output) 