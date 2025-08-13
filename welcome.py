import streamlit as st


st.title("MAKING YOUR OWN TEXT FILE")

# Bigger input box
text_data = st.text_area("", placeholder="Enter some text here", height=200)

# List inputs
t1 = st.text_input("", placeholder='list 1')
t2 = st.text_input("", placeholder='list 2')
t3 = st.text_input("", placeholder='list 3')
t4 = st.text_input("", placeholder='list 4')
t5 = st.text_input("", placeholder='list 5')

col1,col2,col3 = st.columns(3)

col1.text_input('','first name')
col2.text_input('','middle name')
col3.text_input('','last name')

# # Format list neatly
# t = f"""Your list was:
# 1. {t1}
# 2. {t2}
# 3. {t3}
# 4. {t4}
# 5. {t5}
# """

t = f"""{text_data}
 \n{t1}
 \n{t2}
 \n{t3}
 \n{t4}
 \n{t5}
"""
st.write(t)

# Download buttons
st.download_button("Download TXT", data=t, file_name="myfile.txt")
