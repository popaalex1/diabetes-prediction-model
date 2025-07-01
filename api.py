from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import xgboost as xgb
import joblib

class DiabetesInput(BaseModel):
    Diabetes_012: int
    HighBP: int
    HighChol: int
    CholCheck: int
    BMI: float
    Smoker: int
    Stroke: int
    HeartDiseaseorAttack: int
    PhysActivity: int
    Fruits: int
    Veggies: int
    HvyAlcoholConsump: int
    AnyHealthcare: int
    NoDocbcCost: int
    GenHlth: int
    MentHlth: int
    PhysHlth: int
    DiffWalk: int
    Sex: int
    Age: int
    Education: int
    Income: int

app = FastAPI()
model = joblib.load("diabetes_model.joblib")

@app.post("/predict")
def predict_diabetes(data: DiabetesInput):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}