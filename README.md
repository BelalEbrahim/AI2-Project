# Startup Success Prediction API

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![API Status](https://img.shields.io/endpoint?url=https://shields.io/endpoint)

A machine learning API for predicting startup success using FastAPI, with React and Node.js frontend integration.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Local Deployment](#local-deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features
- Startup success prediction model (Acquired/Closed)
- REST API endpoints with JSON responses
- CORS configured for local development
- Automatic PDF documentation generation
- Sample test scripts for Python and Node.js

## Installation

### Backend Setup
```bash
git clone https://github.com/yourusername/startup-success-prediction.git
cd startup-success-prediction

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd frontend
npm install
```

## API Documentation

Generate PDF documentation:
```bash
python generate_docs.py
```

Key endpoints:
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/predict` | POST | Make prediction with startup data |
| `/categories` | GET | Get category mappings |

Request sample:
```json
{
    "state_code": 0,
    "category_code": 8,
    "age_first_funding_year": 2.0,
    "funding_total_usd": 15000000,
    ...
}
```

## Local Deployment

### Run Services
```bash
# Start API (backend)
uvicorn main:app --reload --port 8000

# Start React frontend (separate terminal)
cd frontend && npm start

# Start Node.js service (separate terminal)
node server.js
```

### Access Points
| Service | URL |
|---------|-----|
| API Docs | http://localhost:8000/docs |
| React App | http://localhost:3000 |
| Node Service | http://localhost:8080 |

## Testing

Python test:
```bash
python test_api.py
```

Node.js test:
```bash
node test_api.js
```

## CORS Configuration
Pre-configured origins:
- http://localhost:3000
- http://localhost:8080
- http://localhost:4200

To modify CORS settings, edit `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[...],
    ...
)
```

## Contributing
1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Open pull request

## License
This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.
