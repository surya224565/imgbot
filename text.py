import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": "Bearer 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"}


uploaded_file = st.file_uploader("Upload an image", type="Image")

def query(image_file):
    response = requests.post(API_URL, headers=headers, data=image_file)
    return response.json()

if st.button('Generate'):
    if uploaded_file is not None:
        image_bytes = uploaded_file.read()
        result = query(image_bytes)