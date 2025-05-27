from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Add this import
from pydantic import BaseModel
import pandas as pd
import joblib
import json

app = FastAPI()

# Load the model and preprocessing artifacts
label_encoders = joblib.load('label_encoders.joblib')
feature_names = joblib.load('feature_names.joblib')
model = joblib.load('decision_tree_model.joblib')

# Define the input data model based on your notebook's features
class InputData(BaseModel):
    state_code: int  # e.g., "CA"
    category_code: int  # e.g., "software"
    age_first_funding_year: float
    age_last_funding_year: float
    relationships: int
    funding_rounds: int
    funding_total_usd: int
    milestones: int
    is_CA: int
    is_NY: int
    is_MA: int
    is_TX: int
    is_otherstate: int
    is_software: int
    is_web: int
    is_mobile: int
    is_enterprise: int
    is_advertising: int
    is_gamesvideo: int
    is_ecommerce: int
    is_biotech: int
    is_consulting: int
    is_othercategory: int
    has_VC: int
    has_angel: int
    has_roundA: int
    has_roundB: int
    has_roundC: int
    has_roundD: int
    avg_participants: float
    is_top500: int
    labels: int



# Add this before defining your routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React default port
        "http://localhost:8080",  # Common Node port
        "http://localhost:4200"   # Angular default port
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input to dictionary
        input_dict = data.dict()

        # Encode categorical features
        for col in ['state_code', 'category_code']:
            le = label_encoders[col]
            if input_dict[col] in le.classes_:
                input_dict[col] = le.transform([input_dict[col]])[0]
            else:
                raise HTTPException(status_code=400, detail=f"Unknown category for {col}: {input_dict[col]}")

        # Create DataFrame with correct feature order
        input_df = pd.DataFrame([input_dict], columns=feature_names)

        # Make prediction
        prediction = model.predict(input_df)[0]
        prediction_text = "Success (Acquired)" if prediction == 1 else "Failure (Closed)"

        return {"prediction": prediction_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/categories")
def get_categories():
    """Return available categories and their encoded values from JSON mappings"""
    try:
        with open('label_mappings.json', 'r') as f:
            label_mappings = json.loads(f.read())
            
        return {
            "state_codes": label_mappings.get("state_code", {}),
            "categories": label_mappings.get("category_code", {}),
            "status_labels": label_mappings.get("status", {})
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading categories: {str(e)}")


from fastapi.responses import FileResponse
import os
from generate_docs import create_api_documentation  # Proper import
@app.get("/docs", response_class=FileResponse)
async def get_api_documentation():
    """Serve generated PDF documentation"""
    docs_path = "docs/API_Documentation.pdf"
    
    # Generate PDF if it doesn't exist or is outdated
    if not os.path.exists(docs_path):
        generated_path = create_api_documentation()
        os.rename(generated_path, docs_path)  # Maintain consistent filename
    
    return FileResponse(
        path=docs_path,
        media_type='application/pdf',
        filename="API_Documentation.pdf"
    )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)