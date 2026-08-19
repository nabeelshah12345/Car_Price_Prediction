

import joblib
from pathlib import Path
import pandas as pd 

def load_model_things():
    
    BASE_DIR = Path(__file__).resolve().parent.parent

    model = joblib.load(BASE_DIR / "car_price_model.pkl")
    scaler = joblib.load(BASE_DIR / "scaler.pkl")
    model_columns = joblib.load(BASE_DIR / "columns.pkl")

    return model, scaler, model_columns





def preprocess(payload: dict, scaler, model_columns) -> pd.DataFrame:
  
    df = pd.DataFrame([payload])

    categorical_cols = ["model", "transmission", "fuelType"]
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)


    for col in model_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[model_columns]

    numeric_cols = ["mileage", "mpg", "engineSize"]
    df_encoded[numeric_cols] = scaler.transform(df_encoded[numeric_cols])

    return df_encoded


def predict_price(payload: dict, model, scaler, model_columns) -> float:
    X = preprocess(payload, scaler, model_columns)
    pred = model.predict(X)[0]
    return float(pred)



