import streamlit as st
import segno
import io
from src.database.db import get_registrations
from reportlab.pdfgen import canvas
from io import BytesIO
import supabase
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from src.ui.base_layout import style_base_layout


def generate_qr(data_string):
    qr = segno.make(data_string)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=5)
    return out.getvalue()

def generate_receipt_reportlab(fullname, email, teamname, amount="Rs. 100.00"):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=letter,
        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'InvoiceTitle', parent=styles['Heading1'], fontSize=22, leading=28,
        textColor=colors.HexColor("#FF4B4B"), alignment=1, spaceAfter=5
    )
    subtitle_style = ParagraphStyle(
        'InvoiceSub', parent=styles['Normal'], fontSize=10, leading=14,
        textColor=colors.HexColor("#646464"), alignment=1, spaceAfter=20
    )
    heading_style = ParagraphStyle(
        'SectionHeading', parent=styles['Heading2'], fontSize=12, leading=16, spaceAfter=8
    )
    text_style = ParagraphStyle(
        'BodyTextCustom', parent=styles['Normal'], fontSize=10, leading=14
    )
    amount_text_style = ParagraphStyle(
        'AmountTextCustom', parent=text_style, alignment=2 # Right-aligned
    )
    status_style = ParagraphStyle(
        'StatusText', parent=styles['Normal'], fontSize=10, leading=14,
        textColor=colors.HexColor("#2E7D32"), fontName="Helvetica-Bold"
    )

    story = []
    story.append(Paragraph("GET SET LEARN HACKATHON", title_style))
    story.append(Paragraph("Official Registration & Payment Receipt", subtitle_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("<b>Receipt To:</b>", heading_style))
    story.append(Paragraph(f"<b>Participant Name:</b> {fullname}", text_style))
    story.append(Paragraph(f"<b>Email Address:</b> {email}", text_style))
    story.append(Paragraph(f"<b>Registered Team:</b> {teamname}", text_style))
    
    story.append(Paragraph("<b>Payment Status:</b> PAID / CONFIRMED", status_style))
    story.append(Spacer(1, 20))
    
    table_data = [
        [Paragraph("<b>Description</b>", text_style), Paragraph("<b>Amount</b>", amount_text_style)],
        [Paragraph("Hackathon Entry Fee (Team Registration)", text_style), Paragraph(amount, amount_text_style)],
        [Paragraph("<b>Total Paid</b>", text_style), Paragraph(f"<b>{amount}</b>", amount_text_style)]
    ]
    
    item_table = Table(table_data, colWidths=[380, 150])
    item_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.HexColor("#F0F2F6")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#DDDDDD")),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(item_table)
    story.append(Spacer(1, 40))
    
    footer_style = ParagraphStyle('Footer', parent=styles['Normal'], alignment=1, textColor=colors.gray, fontSize=8, leading=10)
    story.append(Paragraph("This is a computer-generated invoice document. No physical signature is required.", footer_style))
    
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()


def pay_screen():
    style_base_layout()
    reg_id = st.session_state.get("current_reg_id")
    db_user_data = get_registrations(reg_id)
    
    if db_user_data:
        fullname = db_user_data.get("team_leader_name", "Participant")
        email = db_user_data.get("team_leader_email", "N/A")
        teamname = db_user_data.get("team_name", "Team")
    else:
        fullname = st.session_state.get("reg_fullname", "Participant")
        email = st.session_state.get("reg_email", "N/A")
        teamname = st.session_state.get("reg_teamname", "Team")

    style_base_layout() 
    
    col1, col2 = st.columns(2)
    with col1:
        st.header("Please Pay to Proceed")
        qr_bytes = generate_qr("upi://pay?pa=bscit.dhruvbendre@oksbi&pn=Hackathon&am=100") 
        st.image(qr_bytes, caption="Scan using any UPI App", width=250)
    with col2:
        st.subheader("Please read all the rules and regulations carefully")
        st.write("1. Late submissions will not be accepted.")
        st.write("2. Ensure all code is uploaded to your repository before the deadline.")
        st.write("3  only available for kids no adult can participate")
        st.write("4  any kind of misbehaving or mischeif will lead to disqualification")

    if "payment_done" not in st.session_state:
        st.session_state.payment_done = False

    col3, col4 = st.columns(2)
    
    with col3:
    # Clicking this button flips our session state variable to True
        if st.button("Payment Complete", width="stretch", key="payment_btn"):
            st.session_state.payment_done = True
            st.rerun()
    with col4:
    # If payment is successful, render the Download button on the same line instantly!
        if st.session_state.payment_done:
            # Generate the data right before providing it to the download button
            receipt_data = generate_receipt_reportlab(fullname, email, teamname)
            
            # In Streamlit, st.download_button handles its own click automatically! 
            # Clicking it downloads the file immediately.
            st.download_button(
                label="Download Receipt",
                data=receipt_data,
                file_name=f"Receipt_{teamname.replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="receipt_download_btn"
            )
            
            # Trigger celebrations and clear the page loop state
            st.balloons()
            st.session_state.type = None
            
            # Reset the state variable so they don't get stuck in a loops cycle next time
            st.session_state.payment_done = False