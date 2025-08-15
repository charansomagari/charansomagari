import streamlit as st
from datetime import date
today = date.today()

st.title('Welcome')

col1,col2,col3 = st.columns(3)

name = col1.text_input("",placeholder = "please enter your name")

if name == "":
  st.write()
else:
  st.write(f'''Hello {name}, hope you are having a good day, if you want to know about any information about Ipl teams , please select the team in 
  drop down list''')


ipl_teams = ["Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore", 
                 "Kolkata Knight Riders", "Sunrisers Hyderabad", "Delhi Capitals", 
                 "Rajasthan Royals", "Lucknow Super Giants"]
    
selected_team = st.selectbox("Select a team:", ipl_teams)

ipl_info = {
        "Mumbai Indians": "5-time IPL champions.",
        "Chennai Super Kings": "5-time IPL champions.",
        "Royal Challengers Bangalore": "1-time IPL champion.",
        "Kolkata Knight Riders": "3-time IPL champions.",
        "Sunrisers Hyderabad": "2-time IPL champions.",
        "Delhi Capitals": "No cup Yet",
        "Rajasthan Royals": "1-time IPL champion.",
        "Lucknow Super Giants": "No cup Yet.",
        "Kings 11 Punjab" : "No cup Yet."
    }

col1, col2, col3 = st.columns([1, 3, 1])  # Wider middle column
col2.header(ipl_info[selected_team])






