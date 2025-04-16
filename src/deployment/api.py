from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
from typing import List, Dict, Any

from .model_loader import ModelLoader
from .predict import Predictor

app = FastAPI(title="Financial AutoML API")
model_loader = ModelLoader()
predictor = Predictor()

class PredictionInput(BaseModel):
    features: Dict[str, Any]

class PredictionOutput(BaseModel):
    prediction: float
    explanation: Dict[str, float]

@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    try:
        # Convert input to DataFrame
        df = pd.DataFrame([input_data.features])
        
        # Make prediction
        prediction = predictor.predict(df)
        
        # Get explanation
        explanation = predictor.explain(df)
        
        return PredictionOutput(
            prediction=float(prediction[0]),
            explanation=explanation
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/model/info")
async def model_info():
    return {
        "model_type": predictor.model_type,
        "features": predictor.feature_names,
        "metrics": predictor.model_metrics
    }