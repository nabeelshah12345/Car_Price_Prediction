# 🚗 Car Price Prediction

An end-to-end Machine Learning project that predicts used car prices based on vehicle specifications. The project includes a trained ML model, a **FastAPI backend** for serving predictions, and a **Streamlit frontend** for interacting with the model.

## 📌 Project Overview

This project demonstrates how a Machine Learning model can be integrated into a complete application rather than being limited to a notebook.

Users can provide car details through the Streamlit interface, which sends the data to the FastAPI backend. The backend preprocesses the input and uses the trained model to generate a predicted car price.

## ✨ Features

* 🚗 Used car price prediction
* 🤖 Machine Learning regression model
* ⚡ FastAPI REST API
* 🎨 Streamlit frontend
* 🔄 Automated preprocessing and feature encoding
* 📊 Feature scaling using `StandardScaler`
* 💾 Saved model and preprocessing artifacts using Joblib
* 📚 Interactive FastAPI API documentation with Swagger UI
* 🌐 Deployed application

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Joblib**
* **FastAPI**
* **Pydantic**
* **Uvicorn**
* **Streamlit**

## 🧠 Machine Learning

The model was trained using used-car data and the input features were processed before training.

The preprocessing pipeline includes:

* Categorical feature encoding using One-Hot Encoding
* Numerical feature scaling
* Feature alignment with the features used during model training
* Model prediction using the trained regression model

The trained model and preprocessing components are saved using Joblib:

```text
car_price_model.pkl
scaler.pkl
columns.pkl
```

## 🔌 FastAPI Backend

FastAPI is used to create the backend API responsible for receiving car information and returning the predicted price.


## 🎨 Streamlit Frontend

Streamlit provides the user interface where users can enter the required car specifications and receive a predicted price without directly interacting with the API.



## 🌐 Deployment

The project has been deployed with a separate frontend and backend architecture:

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Machine Learning Model:** Scikit-learn

This separation keeps the user interface and prediction API independent and demonstrates a more realistic ML application structure.

## 📚 What I Learned

Through this project, I gained practical experience in:

* Building an end-to-end Machine Learning application
* Serving ML models through FastAPI
* Creating APIs for model inference
* Handling input validation with Pydantic
* Maintaining consistent preprocessing between training and prediction
* Saving and loading ML artifacts with Joblib
* Connecting a frontend with a backend API
* Deploying a Machine Learning application

## 👨‍💻 Author

**Nabeel Shahid**

BS Computer Science Student | Machine Learning & AI Enthusiast

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.
