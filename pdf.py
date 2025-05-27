from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def create_api_documentation():
    # Create PDF document
    file_name = f"API_Documentation_{datetime.now().strftime('%Y%m%d')}.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    
    # Content styling
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    story.append(Paragraph("<b>Startup Success Prediction API Documentation</b>", styles['Title']))
    story.append(Spacer(1, 12))
    
    # API Endpoints
    endpoints = [
        ("POST /predict", "Make prediction with startup data"),
        ("GET /categories", "Get available category mappings")
    ]
    
    for endpoint, description in endpoints:
        story.append(Paragraph(f"<b>{endpoint}</b>", styles['Heading2']))
        story.append(Paragraph(description, styles['BodyText']))
        story.append(Spacer(1, 8))
    
    # Request Example
    story.append(Paragraph("<b>Example Request</b>", styles['Heading2']))
    story.append(Paragraph('''{
    "state_code": 0,
    "category_code": 8,
    "age_first_funding_year": 2.0,
    ...}''', styles['Code']))
    
    # Response Example
    story.append(Paragraph("<b>Example Response</b>", styles['Heading2']))
    story.append(Paragraph('''{
    "prediction": "Success (Acquired)"
}''', styles['Code']))
    
    # Generate PDF
    doc.build(story)
    print(f"PDF created: {file_name}")

if __name__ == "__main__":
    create_api_documentation()