import streamlit as st
from datetime import date
today = date.today()

st.title('Welcome')

col1,col2,col3 = st.columns(3)

name = col1.text_input("",placeholder = "please enter your name")

if name == "":
  st.write()
else:
  st.write(f"Hello {name}, hope you are having a good day")



