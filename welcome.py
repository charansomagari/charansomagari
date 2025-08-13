import streamlit as st
from datetime import date

today = date.today()
c1,c2,c3 = st.columns([1,2,1])

c1.title("Hello")
c2.title(today)

if st.button('welcome'):
  st.write('welcome to this page, this page is under building, please visit again')

