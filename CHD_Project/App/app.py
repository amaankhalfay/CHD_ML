import streamlit as st
import joblib
import numpy as np

# LOAD MODEL + FEATURES
model = joblib.load("CHD_Project/Model/chd_model.pkl")
features = joblib.load("CHD_Project/Model/features.pkl")

st.title("❤️ CHD Risk Prediction System")
st.subheader("🩺 Enter Patient Details")

# INPUTS (ALL FEATURES)

male = st.selectbox("Sex", ["Female", "Male"])
male = 1 if male == "Male" else 0

age = st.number_input("Age", 20, 100, 40)
education = st.selectbox("Education Level", [
    "Some High School",
    "High School Graduate",
    "Some College",
    "College Graduate"
])

education_map = {
    "Some High School": 1,
    "High School Graduate": 2,
    "Some College": 3,
    "College Graduate": 4
}

education = education_map[education]

currentSmoker = st.selectbox("Current Smoker", ["No", "Yes"])
currentSmoker = 1 if currentSmoker == "Yes" else 0

cigsPerDay = st.number_input("Cigarettes per day", 0, 50, 0)

BPMeds = st.selectbox("On BP Medication", ["No", "Yes"])
BPMeds = 1 if BPMeds == "Yes" else 0

prevalentStroke = st.selectbox("Stroke History", ["No", "Yes"])
prevalentStroke = 1 if prevalentStroke == "Yes" else 0

prevalentHyp = st.selectbox("Hypertension", ["No", "Yes"])
prevalentHyp = 1 if prevalentHyp == "Yes" else 0

diabetes = st.selectbox("Diabetes", ["No", "Yes"])
diabetes = 1 if diabetes == "Yes" else 0

totChol = st.number_input("Cholesterol", 100, 400, 200)

sysBP = st.number_input("Systolic BP", 80, 200, 120)
diaBP = st.number_input("Diastolic BP", 50, 130, 80)

BMI = st.number_input("BMI", 15.0, 50.0, 25.0)

heartRate = st.number_input("Heart Rate", 40, 120, 70)

glucose = st.number_input("Glucose", 70, 300, 100)

# PREDICT
if st.button("Predict"):

    input_data = np.array([[male, age, education, currentSmoker, cigsPerDay,
                            BPMeds, prevalentStroke, prevalentHyp, diabetes,
                            totChol, sysBP, diaBP, BMI, heartRate, glucose]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of CHD")
    else:
        st.success("✅ Low Risk of CHD")