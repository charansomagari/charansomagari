import streamlit as st

text_data = "Hello Streamlit!"
st.download_button("Download TXT", data=text_data, file_name="myfile.txt")
