import streamlit as st

st.title('My first app')
st.header('This is a header')

image = st.file_uploader('Upload a file')
# st.image(image)