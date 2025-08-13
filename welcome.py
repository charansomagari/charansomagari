import streamlit as st

col1,col2,col3 = st.columns(2)
col2.title("YOUT TEXT MAKER")
text_data = st.text_input("",placeholder = "enter some text here")
st.download_button("Download TXT", data=text_data, file_name="myfile.txt")
