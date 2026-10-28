import streamlit as st
import joblib

model = joblib.load("spam_model (1).pkl")
vec = joblib.load("vectorizer (1).pkl")

st.title("Email Spam Detector")
text = st.text_area("Enter email text here", height=200)

if st.button("Check"):
    if text.strip() == "":
        st.warning("Please enter some text")
    elif model.predict(vec.transform([text]))[0] == 1:
        st.error("This is SPAM")
    else:
        st.success("This is NOT spam (Ham)")
