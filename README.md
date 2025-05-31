```markdown
# Startup Success Prediction API

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![API Status](https://img.shields.io/endpoint?url=https://shields.io/endpoint)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)

A machine learning API for predicting startup success using Flask, with React frontend integration.

## Table of Contents
- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Local Deployment](#local-deployment)
- [Testing](#testing)
- [CORS Configuration](#cors-configuration)
- [Contributing](#contributing)
- [License](#license)

## Features
- 🚀 Startup success prediction model (Acquired/Closed)
- 📡 REST API endpoints with JSON responses
- 🔒 Automatic CORS configuration
- 📄 PDF documentation generation
- 🧪 Comprehensive test script with fallback data
- 📊 Detailed error handling
- 🔄 Simple deployment with Flask

## Quick Start
```bash
# Clone repository
git clone https://github.com/BelalEbrahim/AI2-Project.git
cd AI2-Project

# Setup environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/MacOS

# Install dependencies
pip install -r requirements.txt

# Start server
python app.py
```

## Installation
```bash
# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Generate documentation
python generate_docs.py
```

## API Documentation

### Endpoints
| Endpoint        | Method | Description                          |
|-----------------|--------|--------------------------------------|
| `/predict`      | POST   | Make prediction with startup data    |
| `/categories`   | GET    | Get category mappings                |
| `/api-docs-pdf` | GET    | Download PDF documentation           |

### Example Request
```json
{
    "state_code": 2,
    "category_code": 30,
    "age_first_funding_year": 2.0,
    "funding_total_usd": 15000000,
    "...": "..."
}
```

### Example Response
```json
{
    "prediction": "acquired",
    "confidence": 0.87,
    "status_code": 0
}
```

## Local Deployment
```bash
# Start backend API
python app.py

# Access endpoints:
curl http://localhost:5000/categories
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "@data.json"
```

## Testing
```bash
# Run test script
python test_api.py

# Manual test with PowerShell
Invoke-WebRequest -Uri http://localhost:5000/predict -Method POST `
    -Headers @{"Content-Type"="application/json"} `
    -Body (Get-Content -Raw -Path .\data.json)
```

## CORS Configuration
CORS is enabled by default. To customize, edit `app.py`:
```python
# Configure specific origins
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://localhost:8080"]}})
```

## Contributing
1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Description'`
4. Push to branch: `git push origin feature-name`
5. Open pull request

**Quality Standards:**
- Maintain 90%+ test coverage
- PEP8 compliant code
- Update documentation with changes

## License
This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

**Maintainer**: Belal Ebrahim  
**GitHub**: https://github.com/BelalEbrahim/AI2-Project/tree/DT_Deployment  
**Documentation**: http://localhost:5000/api-docs-pdf
``` 

This README includes:
1. Updated framework information (Flask instead of FastAPI)
2. Simplified setup instructions
3. Correct default port (5000)
4. Removed Node.js-specific content
5. Updated testing section with PowerShell example
6. Current CORS configuration
7. Direct link to your project branch
8. Clean, single-tab format as requested

All sections are properly formatted with clear headings and consistent styling. The documentation focuses on the current Flask implementation while maintaining all essential information for developers.
