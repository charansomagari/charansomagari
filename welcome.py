import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.title("📄 Text Poster PDF Creator (No ReportLab)")

# User input
user_text = st.text_area("Enter text for the poster:", "Enter some text!")

# Size & font settings
width = st.number_input("Image Width (px)", 200, 3000, 800)
height = st.number_input("Image Height (px)", 200, 3000, 400)
font_size = st.slider("Font Size", 10, 300, 90)
text_color = st.color_picker("Pick Text Color", "#000000")
bg_color = st.color_picker("Pick Background Color", "#FFFFFF")

if st.button("Generate PDF"):
    # Create blank image
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Center text
    text_bbox = draw.textbbox((0, 0), user_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.text((x, y), user_text, fill=text_color, font=font)

    # Save as PDF in memory
    pdf_bytes = io.BytesIO()
    img.save(pdf_bytes, format="PDF")
    pdf_bytes.seek(0)

    # Download button
    st.download_button(
        label="📥 Download PDF Poster",
        data=pdf_bytes,
        file_name="poster.pdf",
        mime="application/pdf"
    )
