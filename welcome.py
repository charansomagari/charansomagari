import streamlit as st

col1,col2,col3 = st.columns(3)

with col2:
  st.header("YOUT TEXT MAKER")
text_data = st.text_area("",placeholder = "enter some text here", height = 200)
st.download_button("Download TXT", data=text_data, file_name="myfile.txt")
