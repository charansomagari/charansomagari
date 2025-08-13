import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import io

st.title("📝 Custom Text Poster PDF Creator")

# User text
user_text = st.text_area("Enter text for the poster:", "Enter some text!")

# Font size
font_size = st.slider("Font Size", 10, 100, 40)

# Text color
text_color = st.color_picker("Pick Text Color", "#000000")

if st.button("Generate PDF"):
    # Create PDF in memory
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=A4)

    # Get page width/height
    width, height = A4

    # Set font
    c.setFont("Helvetica-Bold", font_size)
    c.setFillColor(HexColor(text_color))

    # Calculate position (centered)
    text_width = c.stringWidth(user_text, "Helvetica-Bold", font_size)
    x = (width - text_width) / 2
    y = height / 2

    # Draw text
    c.drawString(x, y, user_text)

    # Save PDF
    c.showPage()
    c.save()

    # Move to start of file
    pdf_buffer.seek(0)

    # Download button
    st.download_button(
        label="📥 Download PDF Poster",
        data=pdf_buffer,
        file_name="poster.pdf",
        mime="application/pdf"
    )
