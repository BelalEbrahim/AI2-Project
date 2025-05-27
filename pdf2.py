from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import datetime
import os

def create_api_docs():
    # Create PDF directory if not exists
    if not os.path.exists('docs'):
        os.makedirs('docs')
    
    filename = f"docs/API_Documentation_{datetime.now().strftime('%Y%m%d')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Custom styles
    styles.add(ParagraphStyle(
        name='Title',
        parent=styles['Heading1'],
        fontSize=18,
        alignment=1,
        spaceAfter=14
    ))
    
    styles.add(ParagraphStyle(
        name='Section',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=12,
        spaceAfter=6
    ))
    
    # Title
    story.append(Paragraph("Startup Success Prediction API Documentation", styles['Title']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Italic']))
    story.append(Spacer(1, 0.5*inch))
    
    # API Endpoints
    content = [
        ("API Endpoints", [
            "POST /predict",
            "• Description: Make prediction for startup success",
            "• Content-Type: application/json",
            "• Request Body Parameters:",
            "  - state_code (int): Encoded state value",
            "  - category_code (int): Encoded category value",
            "  - 20+ numerical features (see full list in repository)",
            "• Response: {'prediction': 'Success (Acquired)' | 'Failure (Closed)'}",
            "",
            "GET /categories",
            "• Description: Get category mappings",
            "• Response: JSON with state codes, categories, and status labels"
        ]),
        ("Local Development", [
            "1. Clone repository: git clone https://github.com/yourusername/startup-success-prediction.git",
            "2. Install dependencies:",
            "   - Backend: pip install -r requirements.txt",
            "   - Frontend: npm install (in frontend directory)",
            "3. Run services:",
            "   - API: uvicorn main:app --reload",
            "   - React: npm start",
            "   - Node: node server.js",
            "4. Access endpoints:",
            "   - API Docs: http://localhost:8000/docs",
            "   - React App: http://localhost:3000"
        ]),
        ("CORS Configuration", [
            "Pre-configured for local development:",
            "- http://localhost:3000 (React)",
            "- http://localhost:8080 (Node.js)",
            "- http://localhost:4200 (Angular)"
        ])
    ]
    
    # Add content to PDF
    for section, items in content:
        story.append(Paragraph(section, styles['Section']))
        for item in items:
            story.append(Paragraph(item, styles['BodyText']))
            story.append(Spacer(1, 0.1*inch))
        story.append(Spacer(1, 0.3*inch))
    
    doc.build(story)
    print(f"PDF documentation generated: {filename}")

if __name__ == "__main__":
    create_api_docs()