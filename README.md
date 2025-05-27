# Startup Success Prediction API

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![API Status](https://img.shields.io/endpoint?url=https://shields.io/endpoint)
![Build Status](https://img.shields.io/github/actions/workflow/status/yourusername/startup-success-prediction/main.yml)
![Coverage](https://img.shields.io/badge/coverage-85%25-green)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)

A machine learning API for predicting startup success using FastAPI, with React and Node.js frontend integration.

![System Architecture](https://via.placeholder.com/800x400.png?text=System+Architecture+Diagram)

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
- 🔒 CORS configured for local development
- 📄 Automatic PDF documentation generation
- 🧪 Sample test scripts for Python and Node.js
- 📊 Comprehensive error handling
- 🔄 Continuous integration ready

## Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/startup-success-prediction.git
cd startup-success-prediction

# Setup and launch (Linux/macOS)
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Installation

### Backend Setup
```bash
git clone https://github.com/yourusername/startup-success-prediction.git
cd startup-success-prediction

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

### Frontend Setup
```bash
cd frontend

# Install Node.js dependencies
npm install

# Start development server
npm start
```

## API Documentation

### Access Documentation
```bash
# Access interactive API docs
http://localhost:8000/docs

# Download PDF documentation
http://localhost:8000/api-docs-pdf
```

### Key Endpoints
| Endpoint        | Method | Description                          | Authentication |
|-----------------|--------|--------------------------------------|----------------|
| `/predict`      | POST   | Make prediction with startup data    | None           |
| `/categories`   | GET    | Get category mappings                | None           |
| `/healthcheck`  | GET    | System status monitoring             | None           |

### Example Request
```json
{
    "state_code": 0,
    "category_code": 8,
    "age_first_funding_year": 2.0,
    "age_last_funding_year": 6.0,
    "relationships": 3,
    "funding_rounds": 4,
    "funding_total_usd": 15000000,
    "milestones": 2,
    "...": "..."
}
```

### Example Response
```json
{
    "prediction": "Success (Acquired)",
    "confidence": 0.87,
    "model_version": "1.0.1"
}
```

## Local Deployment

### Service Management
```bash
# Start API (backend)
uvicorn main:app --reload --port 8000

# Start React frontend (separate terminal)
cd frontend && npm start

# Start Node.js service (separate terminal)
node server.js
```

### Access Points
| Service        | URL                              | Description                |
|----------------|----------------------------------|----------------------------|
| API Docs       | http://localhost:8000/docs      | Interactive Swagger UI     |
| ReDoc          | http://localhost:8000/redoc     | Alternative documentation  |
| React App      | http://localhost:3000           | Frontend interface         |
| Node Service   | http://localhost:8080           | Backend service endpoints  |

## Testing

### Python Tests
```bash
# Run API tests
python -m pytest tests/

# Execute sample prediction
python test_api.py
```

### Node.js Tests
```bash
# Run service tests
npm test

# Execute sample request
node test_api.js
```

### Expected Test Output
```
API Status: 200 OK
Prediction: Success (Acquired)
Test Coverage: 92%
```

## CORS Configuration

### Pre-configured Origins
```python
[
    "http://localhost:3000",  # React development server
    "http://localhost:8080",  # Node.js service
    "http://localhost:4200"   # Angular development
]
```

### Custom Configuration
Edit `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Contributing

### Development Workflow
1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Open pull request

### Quality Standards
- 90%+ test coverage
- PEP8 compliant code
- Type hints for all functions
- Documentation updates included

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

**Maintainer**: Your Name \<your.email@example.com>  
**CI/CD Status**: [View Pipeline](https://github.com/yourusername/startup-success-prediction/actions)  
**Documentation**: [Full API Docs](https://yourusername.github.io/startup-success-prediction/)
