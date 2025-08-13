import streamlit as st
from datetime import date
import random as rm
today = date.today()
c1,c2,c3 = st.columns([1,2,1])

c1.title("Hello")
c3.title(today)

if st.button('welcome'):
  st.write('welcome to this page, this page is under building, please visit again')

if 'a' not in st.session_state:
    st.session_state.a = 0

if st.button('ok'):
    st.session_state.a += 1

st.write(st.session_state.a)

if 'b' not in st.session_state:
  st.session_state.b = []

t = st.text_input('enter number')

r = rm.randint(1,1)

if int(t) == r:
  st.write('yes')
