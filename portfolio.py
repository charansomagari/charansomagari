import streamlit as st

st.header('CHARAN KUMAR REDDY SOMAGARI')

import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="My Portfolio", layout="wide")

# --- HEADER ---
st.markdown("<h1 style='text-align: center;'>Your Name</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Senior Data Analyst | PySpark | Azure</h3>", unsafe_allow_html=True)

# --- ABOUT ME ---
col1, col2 = st.columns([1, 3])
with col1:
    st.image("your_photo.jpg", width=200)
with col2:
    st.write("""
    Hi, I'm [Your Name], a Senior Data Analyst with over 6 years of experience in ...
    """)

# --- SKILLS ---
st.subheader("Skills")
skill1, skill2, skill3, skill4 = st.columns(4)
skill1.metric("SQL", "Expert")
skill2.metric("Tableau", "Advanced")
skill3.metric("PySpark", "Advanced")
skill4.metric("Azure", "Intermediate")

# --- PROJECTS ---
st.subheader("Projects")
p1, p2, p3 = st.columns(3)
p1.image("project1.png")
p1.markdown("[View Project](https://github.com/...)")

# --- CONTACT ---
st.subheader("Contact")
st.write("📧 Email: your.email@example.com")
st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile)")
