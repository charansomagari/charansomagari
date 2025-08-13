import streamlit as st
from fpdf import FPDF
import io

st.title("📄 PDF Poster Creator (No PIL)")

# User inputs
user_text = st.text_area("Enter text for the poster:", "Enter some text!")
font_size = st.slider("Font Size", 10, 100, 40)
text_color = st.color_picker("Pick Text Color", "#000000")  # Hex format

if st.button("Generate PDF"):
    # Create PDF
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Convert hex color to RGB
    text_color = text_color.lstrip('#')
    r, g, b = tuple(int(text_color[i:i+2], 16) for i in (0, 2, 4))
    pdf.set_text_color(r, g, b)

    # Set font and size
    pdf.set_font("Helvetica", size=font_size)

    # Calculate vertical position for centering
    page_width = pdf.w
    page_height = pdf.h
    text_width = pdf.get_string_width(user_text)
    x = (page_width - text_width) / 2
    y = page_height / 2

    pdf.set_xy(x, y)
    pdf.cell(text_width, 10, user_text)

    # Save to in-memory bytes
    pdf_bytes = io.BytesIO()
    pdf.output(pdf_bytes)
    pdf_bytes.seek(0)

    # Download button
    st.download_button(
        label="📥 Download PDF Poster",
        data=pdf_bytes,
        file_name="poster.pdf",
        mime="application/pdf"
    )
