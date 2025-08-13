import streamlit as st

col1, col2, col3 = st.columns(3)
col2.header("YOUR TEXT MAKER")

# Bigger input box
text_data = st.text_area("", placeholder="Enter some text here", height=200)

# List inputs
t1 = st.text_area("Item 1", 'list 1')
t2 = st.text_area("Item 2", 'list 2')
t3 = st.text_area("Item 3", 'list 3')
t4 = st.text_area("Item 4", 'list 4')
t5 = st.text_area("Item 5", 'list 5')

# Format list neatly
t = f"""Your list was:
1. {t1}
2. {t2}
3. {t3}
4. {t4}
5. {t5}
"""

# Download buttons
st.download_button("Download TXT", data=text_data, file_name="myfile.txt")
st.download_button("Download List TXT", data=t, file_name="list.txt")
