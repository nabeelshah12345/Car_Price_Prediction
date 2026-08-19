import streamlit as st
import requests


st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")
st.title("🚗 Ford Car Price Prediction")
st.write("Enter Car details : ")

# ---------- API endpoint ----------
API_URL = "https://car-price-prediction-six-xi.vercel.app/predict"

# ---------- Categorical options (schema.py se exact match) ----------
model_options = [
    "B-MAX", "C-MAX", "EcoSport", "Edge", "Escort", "Fiesta", "Focus",
    "Fusion", "Galaxy", "Grand C-MAX", "Grand Tourneo Connect", "KA",
    "Ka+", "Kuga", "Mondeo", "Mustang", "Puma", "Ranger", "S-MAX",
    "Streetka", "Tourneo Connect", "Tourneo Custom"
]
transmission_options = ["Automatic", "Manual", "Semi-Auto"]
fuel_options = ["Diesel", "Electric", "Hybrid", "Petrol"]

# ---------- Input widgets ----------
car_model = st.selectbox("Car Model", model_options)
transmission = st.selectbox("Transmission", transmission_options)
fuel_type = st.selectbox("Fuel Type", fuel_options)

mileage = st.number_input("Mileage (miles driven)", min_value=0.0, value=15000.0)
mpg = st.number_input("MPG (fuel efficiency)", min_value=0.0, value=55.0)
engine_size = st.number_input("Engine Size (litres)", min_value=0.1, max_value=6.0, value=1.0)
car_age = st.number_input("Car Age (years)", min_value=0, max_value=30, value=3)



GBP_TO_PKR = 375.75
# ---------- Predict button ----------
if st.button("Predict Price"):
    payload = {
        "mileage": mileage,
        "mpg": mpg,
        "engineSize": engine_size,
        "car_age": car_age,
        "model": car_model,
        "transmission": transmission,
        "fuelType": fuel_type
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json() 
            price_gdp = result["prediction"] # price in pounds
            price_pkr = price_gdp * GBP_TO_PKR
            st.success(f"Estimated Price: Rs {price_pkr:,.0f} or (≈ £{price_gdp:,.2f})")
        else:
            st.error(f"Error from API: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Fast API Server not Working Properly")
        
        
# cd "D:\coding\Python\ALL ML Projects\Car_Price_Prediction"
# python -m streamlit run streamlit_app.py