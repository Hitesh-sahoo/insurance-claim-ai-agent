import streamlit as st
from main import run_pipeline

st.title("🧠 Insurance Claim AI Agent")

uploaded_file = st.file_uploader("Upload FNOL PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    result = run_pipeline("temp.pdf")

    st.success("Processing completed ✅")
    st.json(result)