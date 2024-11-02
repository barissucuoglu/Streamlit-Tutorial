import streamlit as st
import spacy

nlp = spacy.load("en_core_web_lg")

def extract_entities(ent_types, text):
    results = []
    doc = nlp(text=text)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            results.append((ent.text, ent.label_))
    return (results)

st.title("Forms in Streamlit")

form1 = st.sidebar.form(key="Options")
form1.header("Params")

ent_types = form1.multiselect("Select the entities you want to extract", ["PERSON", "ORG", "GPE"])
form1.form_submit_button("Click Me")

text = st.text_area("Sample Text", "James enjoys playing basketball in Florida for the Salvation Army.")
hits = extract_entities(ent_types, text)
st.write(hits)