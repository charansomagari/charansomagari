import streamlit as st

text_data = st.text_input("your text maker",placeholder = "enter some text here")
st.download_button("Download TXT", data=text_data, file_name="myfile.txt")
