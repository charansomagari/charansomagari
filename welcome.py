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

# # Format list neatly
# t = f"""Your list was:
# 1. {t1}
# 2. {t2}
# 3. {t3}
# 4. {t4}
# 5. {t5}
# """

t = f"""{text_data},
 {t1}
 {t2}
 {t3}
 {t4}
 {t5}
"""

# Download buttons
st.download_button("Download TXT", data=t, file_name="myfile.txt")
