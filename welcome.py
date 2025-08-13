import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.title("🎨 Custom Text Poster Creator")

# User text
user_text = st.text_area("Enter text for the poster:", "Enter some text!")

# Image settings
width = st.number_input("Image Width (px)", 200, 3000, 800)
height = st.number_input("Image Height (px)", 200, 3000, 400)

# Font settings
font_size = st.slider("Font Size", 10, 300, 90)
text_color = st.color_picker("Pick Text Color", "#000000")
bg_color = st.color_picker("Pick Background Color", "#FFFFFF")

# Generate button
if st.button("Generate Image"):
    # Create blank image
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Load font (change path if needed)
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

    # Show image
    st.image(img, caption="Generated Poster", use_column_width=True)

    # Save as PNG
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()

    # Download button
    st.download_button(
        label="Download Image",
        data=img_bytes,
        file_name="custom_poster.png",
        mime="image/png"
    )
