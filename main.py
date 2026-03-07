from fastapi import FastAPI
from pydantic import BaseModel
from model import detect_anxiety

app = FastAPI(title="AI Exam Anxiety Detector")

class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Exam Anxiety Detector API running"}

@app.post("/predict")
def predict(data: InputText):
    level = detect_anxiety(data.text)
    return {"anxiety_level": level}