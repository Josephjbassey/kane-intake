import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_invoice_pdf(filename="mock_invoices/lagos_logistics_invoice_1113.pdf"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#0f172a'),
        fontName='Helvetica-Bold'
    )
    
    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#475569')
    )

    story.append(Paragraph("TAX INVOICE", title_style))
    story.append(Spacer(1, 10))

    meta_text = """
    <b>Vendor:</b> Lagos Freight & Logistics Ltd<br/>
    <b>Address:</b> 14 Commercial Avenue, Yaba, Lagos, Nigeria<br/>
    <b>Invoice Number:</b> INV-2026-1113<br/>
    <b>Invoice Date:</b> 13 Nov 2026<br/>
    <b>Payment Terms:</b> Due upon receipt
    """
    story.append(Paragraph(meta_text, meta_style))
    story.append(Spacer(1, 20))

    table_data = [
        ["Item / Description", "Qty", "Unit Price", "Total Amount"],
        ["Inter-State Freight Haulage (Lagos -> Abuja)", "1", "NGN 8,500.00", "NGN 8,500.00"],
        ["Secure Pallet Warehousing & Handling", "1", "NGN 4,000.00", "NGN 4,000.00"],
        ["", "", "Grand Total:", "NGN 12,500.00"]
    ]

    t = Table(table_data, colWidths=[260, 50, 100, 120])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f1f5f9')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#0f172a')),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor('#cbd5e1')),
        ('LINEBELOW', (0, -2), (-1, -2), 1, colors.HexColor('#e2e8f0')),
        ('FONTNAME', (2, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(t)
    
    doc.build(story)
    print(f"Generated mock invoice PDF: {filename}")

if __name__ == "__main__":
    generate_invoice_pdf()
