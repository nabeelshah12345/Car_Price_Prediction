

from fastapi import FastAPI
from app.model import load_model_things, predict_price
from fastapi.responses import JSONResponse
from app.schema import car_features, prediction_price 

app = FastAPI(title="Car Price Prediction")



model = None
scaler = None
model_columns = None

@app.on_event("startup")
def start_event():
    global model, scaler, model_columns
    model, scaler, model_columns = load_model_things()



@app.get("/")
def test():
    return JSONResponse(status_code=200, content={"success": True, "Message": "App Run Successfully"})
 

@app.post("/predict", response_model=prediction_price) 
def predict(features:car_features): 
    price = predict_price(features.model_dump(), model, scaler, model_columns)
    return prediction_price(prediction=price)



