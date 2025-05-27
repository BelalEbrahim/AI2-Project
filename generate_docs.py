"""
PDF Documentation Generator for Startup Success Prediction API

This module generates professional API documentation in PDF format using ReportLab.
It includes detailed endpoint descriptions, request/response examples, and setup instructions.
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from datetime import datetime
import os

# Custom style configurations
STYLE_CONFIG = {
    'code_bg_color': colors.Color(0.95, 0.95, 0.95),  # Light gray background
    'border_color': colors.HexColor('#2c3e50'),        # Dark blue border
    'highlight_color': colors.HexColor('#3498db')      # Blue highlight
}

def create_api_documentation():
    """
    Generates comprehensive PDF documentation for the Startup Success Prediction API
    
    Creates a structured PDF document containing:
    - API endpoint specifications
    - Request/response examples
    - Error handling documentation
    - System setup instructions
    - Contact information
    
    The generated PDF is saved in the 'docs' directory with a timestamped filename.
    """
    
    # Create output directory if missing
    if not os.path.exists('docs'):
        os.makedirs('docs')
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"docs/API_Documentation_{timestamp}.pdf"
    
    # Initialize PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Custom style definitions
    styles.add(ParagraphStyle(
        name='CodeBlock',
        parent=styles['Code'],
        backColor=STYLE_CONFIG['code_bg_color'],
        borderColor=STYLE_CONFIG['border_color'],
        borderWidth=1,
        borderPadding=5,
        leftIndent=10,
        spaceAfter=12
    ))
    
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading2'],
        textColor=STYLE_CONFIG['highlight_color'],
        spaceBefore=18,
        spaceAfter=12
    ))

    # -------------------------
    # Title Page
    # -------------------------
    story.append(Paragraph(
        "<b>Startup Success Prediction API</b><br/><br/>Version 1.0.0", 
        styles['Title']
    ))
    story.append(Spacer(1, 24))
    story.append(Paragraph(
        "Comprehensive Documentation for REST Endpoints and System Integration",
        styles['Heading3']
    ))
    story.append(PageBreak())

    # -------------------------
    # Table of Contents
    # -------------------------
    story.append(Paragraph("Table of Contents", styles['Heading1']))
    toc_items = [
        ("1. API Endpoints", 2),
        ("2. Request/Response Examples", 3),
        ("3. Error Handling", 4),
        ("4. System Setup", 5),
        ("5. CORS Configuration", 6),
        ("6. Contact Information", 7)
    ]
    
    for item, page_num in toc_items:
        story.append(Paragraph(
            f'<link href="page{page_num}">{item} - Page {page_num}</link>',
            styles['BodyText']
        ))
    story.append(PageBreak())

    # -------------------------
    # API Endpoints Section
    # -------------------------
    story.append(Paragraph("1. API Endpoints", styles['Heading1']))
    
    endpoints = [
        ("POST /predict", 
         "Submit startup data for success prediction",
         ["state_code (int): Encoded state value",
          "category_code (int): Encoded category value",
          "funding_total_usd (int): Total funding in USD",
          "... (20+ additional features)"]),
         
        ("GET /categories", 
         "Retrieve available category mappings",
         ["Returns JSON with state codes, categories, and status labels"])
    ]
    
    for endpoint, description, params in endpoints:
        story.append(Paragraph(endpoint, styles['SectionHeader']))
        story.append(Paragraph(description, styles['BodyText']))
        if params:
            story.append(Paragraph("<b>Parameters:</b>", styles['BodyText']))
            for param in params:
                story.append(Paragraph(f"• {param}", styles['BodyText']))
        story.append(Spacer(1, 12))

    # -------------------------
    # Request/Response Examples
    # -------------------------
    story.append(PageBreak())
    story.append(Paragraph("2. Request/Response Examples", styles['Heading1']))
    
    # Request Example
    story.append(Paragraph("Sample Prediction Request", styles['SectionHeader']))
    story.append(Paragraph('''{
    "state_code": 0,
    "category_code": 8,
    "age_first_funding_year": 2.0,
    "funding_total_usd": 15000000,
    "milestones": 2,
    ...
}''', styles['CodeBlock']))
    
    # Response Example
    story.append(Paragraph("Success Response", styles['SectionHeader']))
    story.append(Paragraph('''{
    "prediction": "Success (Acquired)",
    "confidence": 0.87
}''', styles['CodeBlock']))
    
    # Error Response
    story.append(Paragraph("Error Response", styles['SectionHeader']))
    story.append(Paragraph('''{
    "detail": "Invalid category code: 25"
}''', styles['CodeBlock']))

    # -------------------------
    # Error Handling Documentation
    # -------------------------
    story.append(PageBreak())
    story.append(Paragraph("3. Error Handling", styles['Heading1']))
    
    errors = [
        ("400 Bad Request", "Invalid request format or parameters"),
        ("422 Validation Error", "Missing required fields or invalid data types"),
        ("500 Internal Server Error", "Unexpected server error")
    ]
    
    for code, description in errors:
        story.append(Paragraph(code, styles['SectionHeader']))
        story.append(Paragraph(description, styles['BodyText']))
        story.append(Spacer(1, 8))

    # -------------------------
    # System Setup Instructions
    # -------------------------
    story.append(PageBreak())
    story.append(Paragraph("4. System Setup", styles['Heading1']))
    
    setup_steps = [
        "1. Clone repository: git clone https://github.com/yourorg/startup-api",
        "2. Install dependencies: pip install -r requirements.txt",
        "3. Start server: uvicorn main:app --reload",
        "4. Access endpoints:",
        "   - API Docs: http://localhost:8000/docs",
        "   - React App: http://localhost:3000"
    ]
    
    for step in setup_steps:
        story.append(Paragraph(step, styles['BodyText']))

    # -------------------------
    # CORS Configuration
    # -------------------------
    story.append(PageBreak())
    story.append(Paragraph("5. CORS Configuration", styles['Heading1']))
    story.append(Paragraph('''Allowed origins:
- http://localhost:3000 (React)
- http://localhost:8080 (Node.js)
- http://localhost:4200 (Angular)''', styles['CodeBlock']))

    # -------------------------
    # Contact Information
    # -------------------------
    story.append(PageBreak())
    story.append(Paragraph("6. Contact Information", styles['Heading1']))
    contacts = [
        ("Support Email", "support@startupapi.com"),
        ("API Documentation", "https://api.startup.com/docs"),
        ("GitHub Repository", "https://github.com/yourorg/startup-api")
    ]
    
    for label, value in contacts:
        story.append(Paragraph(f"<b>{label}:</b> {value}", styles['BodyText']))

    # Generate PDF
    doc.build(story)
    print(f"Successfully generated documentation: {filename}")
    return filename

if __name__ == "__main__":
    create_api_documentation()