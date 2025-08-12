import streamlit as st

st.title("Hello Streamlit 👋")
name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome, {name}!")
st.write('this is awesome')


st.title("👋 Hi, I'm Charan Kumar Reddy")
st.subheader("Senior Data Analyst | Data Engineer | Dashboard Creator")
st.write("6+ years of experience in data analytics, visualization, and cloud technologies.")

st.text_input()
