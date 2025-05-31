Here's your combined code block incorporating all technical instructions from the README into a single cohesive markdown code block:

```markdown
# Startup Success Prediction API

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)  
![License](https://img.shields.io/badge/license-MIT-green)  
![API Status](https://img.shields.io/endpoint?url=https://shields.io/endpoint)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)

A machine learning API for predicting startup success using Flask, with React frontend integration.

## Full Technical Implementation

```bash
# --- Quick Start ---
git clone https://github.com/BelalEbrahim/AI2-Project.git  
cd AI2-Project

# Create and activate environment
python -m venv venv
# Windows
venv\Scripts\activate  
# Linux/MacOS
source venv/bin/activate  

# Install dependencies
pip install -r requirements.txt

# Start server
python app.py

# --- Installation ---
python generate_docs.py  # Generate PDF documentation

# --- Local Deployment ---
# Start backend API
python app.py

# Test endpoints
curl http://localhost:5000/categories
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d "@data.json"

# --- Testing ---
python test_api.py  # Comprehensive test suite

# PowerShell manual test
Invoke-WebRequest -Uri http://localhost:5000/predict \
-Method POST \
-Headers @{"Content-Type"="application/json"} \
-Body (Get-Content -Raw -Path .\data.json)

# --- CORS Configuration ---
# In app.py, modify origins as needed:
CORS(app, resources={
    r"/*": {"origins": ["http://localhost:3000", "http://localhost:8080"]}
})

# --- Example Request JSON ---
{
    "state_code": 2,
    "category_code": 30,
    "age_first_funding_year": 2.0,
    "funding_total_usd": 15000000,
    "...": "..."
}

# --- Example Response ---
{
    "prediction": "acquired",
    "confidence": 0.87,
    "status_code": 0
}
```

## Key Implementation Details
- **Model**: Uses logistic regression and decision tree classifiers
- **Performance**: 
  - Logistic Regression: 68.64% accuracy
  - Decision Tree: 100% accuracy (potential overfitting)
- **Features**: 
  - Funding metrics
  - Milestones
  - Investor relationships
  - Geographic and industry data

## Project Structure
```
AI2-Project/
├── app.py            # Flask API server
├── generate_docs.py  # PDF documentation generator
├── test_api.py       # Test suite
├── data.json         # Sample request data
└── requirements.txt  # Dependencies
```

**Maintainer**: Belal Ebrahim  
**Documentation**: http://localhost:5000/api-docs-pdf  
**Repository**: https://github.com/BelalEbrahim/AI2-Project/tree/DT_Deployment
```

This format:
1. Consolidates all code snippets into one logical flow
2. Maintains separation between different operations using comments
3. Preserves all technical implementation details
4. Maintains proper syntax highlighting
5. Keeps documentation elements intact

Would you like me to adjust any specific sections or formatting?
