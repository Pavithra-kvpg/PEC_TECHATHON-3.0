from fastapi import FastAPI
import pickle, os
import pandas as pd

app = FastAPI()

# Try loading the model safely
model = None
try:
    model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models/oxygen_model.pkl"))
    print("Loading model from:", model_path)
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    print("✅ Model loaded")
except Exception as e:
    print("⚠️ Could not load model:", e)

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.get("/predict")
def predict(steps: int = 24):
    if model is None:
        return {"error": "Model not loaded"}
    forecast = model.forecast(steps)
    dates = pd.date_range(pd.Timestamp.now(), periods=steps, freq="H").strftime("%Y-%m-%d %H:%M").tolist()
    return {"timestamps": dates, "forecast": forecast.tolist()}
