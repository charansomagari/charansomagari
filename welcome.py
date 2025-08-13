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

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.title("Text to Printable Image")

# User enters text
user_text = st.text_input("Enter text to print on image:", "Hello, World!")

# Image size settings
width = st.number_input("Image Width (px)", 200, 2000, 800)
height = st.number_input("Image Height (px)", 200, 2000, 400)

if st.button("Generate Image"):
    # Create a blank white image
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)

    # Load a font (fallback if custom font not available)
    try:
        font = ImageFont.truetype("arial.ttf", 90)  # You can use your own .ttf font
    except:
        font = ImageFont.load_default()

    # Calculate text position (centered)
    text_bbox = draw.textbbox((0,0), user_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Draw text
    draw.text((x, y), user_text, fill="black", font=font)

    # Show image in Streamlit
    st.image(img, caption="Generated Image")

    # Convert to bytes for download
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()

    # Download button
    st.download_button(
        label="Download Image",
        data=img_bytes,
        file_name="printable_text_image.png",
        mime="image/png"
    )

