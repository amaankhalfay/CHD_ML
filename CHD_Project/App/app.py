import streamlit as st
import joblib
import numpy as np

# LOAD MODEL
model = joblib.load("../model/chd_model.pkl")

st.title("❤️ CHD Risk Prediction System")

st.write("Enter patient details:")

# INPUTS
age = st.number_input("Age", 20, 100)
sysBP = st.number_input("Systolic BP")
diaBP = st.number_input("Diastolic BP")
chol = st.number_input("Cholesterol")
glucose = st.number_input("Glucose")
cigs = st.number_input("Cigarettes per day")

# PREDICTION
if st.button("Predict"):
    input_data = np.array([[age, cigs, 0, 0, 0, 0, 0, sysBP, diaBP, 0, 0, glucose, 0, 0, 0]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of CHD")
    else:
        st.success("✅ Low Risk of CHD")