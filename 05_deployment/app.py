from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="API Riesgo Crediticio")

# Cargar artefactos
model = joblib.load("../artifacts/log_reg_model.joblib")
threshold = joblib.load("../artifacts/decision_threshold.joblib")

@app.get("/")
def home():
    return {"status": "API activa"}

@app.post("/predict")
def predict(data: dict):
    X = pd.DataFrame([data])
    prob = model.predict_proba(X)[:, 1][0]
    pred = int(prob >= threshold)

    return {
        "prob_incumplimiento": prob,
        "prediccion": pred
    }