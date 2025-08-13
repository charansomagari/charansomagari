import streamlit as st

col1, col2, col3 = st.columns(3)
col2.header("YOUR TEXT MAKER")

# Bigger input box
text_data = st.text_area("", 
    placeholder="Enter some text here", height=200)

t1 = st.text_area("",'list 1')
t2 = st.text_area("",' list 2')
t3 = st.text_area("",' list 3')
t4 = st.text_area("",' list 4')
t5 = st.text_area("",' list 5')

t = (f"your list was {t1} , {t2}, {t3}, {t4}, {t5}")

# Download button
st.download_button("Download TXT", data=text_data, file_name="myfile.txt")

st.download_button('list',data = t, file_name = 'list.txt')
