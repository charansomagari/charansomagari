import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.title("Create a Text Poster")

# User input
user_text = st.text_area("Enter text for the poster:", "Enter some text!")

width = st.number_input("Image Width (px)", 200, 2000, 800)
height = st.number_input("Image Height (px)", 200, 2000, 400)

if st.button("Generate Image"):
    # Create a blank white image
    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)


try:
    font = ImageFont.truetype("sans-serif.ttf", 90)  # You can use your own .ttf font
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
