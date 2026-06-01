import streamlit as st
import requests

st.title("🤖 Model Information")

response = requests.get(
    "http://127.0.0.1:8000/prediction/model-info"
)

st.json(response.json())
