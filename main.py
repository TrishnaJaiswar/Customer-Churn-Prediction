import streamlit as st
import requests 

st.title("Customer Churn Prediction ")

col1, col2 , col3= st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72)
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])

with col2:
    
    multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"]) 

with col3:
    streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"]) 
    streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"]) 
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"]) 
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"]) 
    payment_method = st.selectbox( "Payment Method", [ "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)" ] ) 
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0) 


total_charges = st.number_input("Total Charges", min_value=0.0)

import requests

if st.button("Predict Churn"):

    data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    if response.status_code == 200:
        result = response.json()

        st.success(f"Prediction: {result['Prediction']}")
        st.info(f"Churn Probability: {result['Churn Probability']}")

    else:
        st.error("Prediction Failed")
        st.write(response.text)