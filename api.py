from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import xgboost as xgb
import joblib

class DiabetesInput(BaseModel):
    Diabetes_012: float
    HighBP: float
    HighChol: float
    CholCheck: float
    BMI: float
    Smoker: float
    Stroke: float
    HeartDiseaseorAttack: float
    PhysActivity: float
    Fruits: float
    Veggies: float
    HvyAlcoholConsump: float
    AnyHealthcare: float
    NoDocbcCost: float
    GenHlth: float
    MentHlth: float
    PhysHlth: float
    DiffWalk: float
    Sex: float
    Age: float
    Education: float
    Income: float

app = FastAPI()
model = joblib.load("diabetes_model.joblib")

@app.post("/predict")
def predict_diabetes(data: DiabetesInput):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}