import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.title("HD Printable Text Poster")

# User input
user_text = st.text_area("Enter text for the poster:", "Hello, World!")

# A4 size in pixels at 300 DPI
A4_WIDTH_PX = 2480
A4_HEIGHT_PX = 3508

# Font size selection
font_size = st.slider("Font Size", 20, 300, 120)

# Text & background colors
text_color = st.color_picker("Text Color", "#000000")
bg_color = st.color_picker("Background Color", "#FFFFFF")

if st.button("Generate Poster"):
    # Create high-res A4 image
    img = Image.new("RGB", (A4_WIDTH_PX, A4_HEIGHT_PX), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Load font (fallback to default if not available)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Center text
    text_bbox = draw.textbbox((0, 0), user_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (A4_WIDTH_PX - text_width) / 2
    y = (A4_HEIGHT_PX - text_height) / 2

    draw.text((x, y), user_text, fill=text_color, font=font)

    # Show preview (scaled down for screen)
    st.image(img.resize((620, 877)), caption="Preview (A4 size, 300 DPI)", use_column_width=False)

    # Save in high quality with 300 DPI
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG", dpi=(300, 300))
    img_bytes = img_bytes.getvalue()

    # Download button
    st.download_button(
        label="Download HD Poster",
        data=img_bytes,
        file_name="printable_poster.png",
        mime="image/png"
    )
