import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title(" Fraud Detection App")

st.write("Enter transaction amount:")

amount = st.number_input("Transaction Amount", min_value=0.0)

if st.button("Check"):

    input_data = np.zeros((1, 30))
    input_data[0, -1] = amount

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error(" Fraudulent Transaction")
    else:
        st.success(" Legitimate Transaction")
        