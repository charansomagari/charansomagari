import streamlit as st

st.title("Hello Streamlit 👋")
name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome, {name}!")
st.write('this is awesome')


st.title("👋 Hi, I'm Charan Kumar Reddy")
st.subheader("Senior Data Analyst | Data Engineer | Dashboard Creator")
st.write("6+ years of experience in data analytics, visualization, and cloud technologies.")

st.text_input('yes')


name = st.text_input("Enter your name",
                     placeholder="Type here...")

age = st.text_input("Enter your age",
                     placeholder="Type here...")

st.header(f"welcome {name}")

# for i in range(9):
#     st.write(i+1)

state = {'':'nothing selected','ANDHRA PRADESH':'AMARAVATHI',
        'TELANGANA':'HYDERABAD'}


sel = st.selectbox('OPTIONS',['','ANDHRA PRADESH','TELANGANA'])

if sel:
    st.write(state[sel])
    

option = st.selectbox(
    "Choose your favorite fruit:",
    ["Apple", "Banana", "Mango", "Orange"]
)
