import streamlit as st
import numpy as np
import pandas as pd
import joblib


model = joblib.load("logistic_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("📉 Customer Churn Prediction App")


gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.selectbox("Has Partner", ["Yes", "No"])
dependents = st.selectbox("Has Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

input_dict = {
    'gender': 1 if gender == "Male" else 0,
    'SeniorCitizen': 1 if senior == "Yes" else 0,
    'Partner': 1 if partner == "Yes" else 0,
    'Dependents': 1 if dependents == "Yes" else 0,
    'tenure': tenure,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'PaperlessBilling': 1 if paperless == "Yes" else 0,
    'Contract_Month-to-month': 0,
    'Contract_One year': 0,
    'Contract_Two year': 0,
}


input_dict[f"Contract_{contract}"] = 1

for col in model_columns:
    if col not in input_dict:
        input_dict[col] = 0


input_df = pd.DataFrame([input_dict])[model_columns]


if st.button("Predict"):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.error("⚠️ This customer is likely to churn.")
    else:
        st.success("✅ This customer is likely to stay.")
