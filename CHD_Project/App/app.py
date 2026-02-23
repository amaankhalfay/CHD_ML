import streamlit as st
import joblib
import numpy as np

# PAGE CONFIG
st.set_page_config(page_title="CHD Prediction", page_icon="❤️", layout="centered")

# LOAD MODEL + FEATURES
model = joblib.load("CHD_Project/Model/chd_model.pkl")
features = joblib.load("CHD_Project/Model/features.pkl")

# HEADER
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>❤️ CHD Risk Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter patient details to assess heart disease risk</p>", unsafe_allow_html=True)

st.divider()

# -------------------- BASIC INFO --------------------
st.subheader("🧍 Basic Information")

col1, col2 = st.columns(2)

with col1:
    male = st.selectbox("Sex", ["Female", "Male"])
    male = 1 if male == "Male" else 0

    age = st.number_input("Age", 20, 100, 40)

    currentSmoker = st.selectbox("Current Smoker", ["No", "Yes"])
    currentSmoker = 1 if currentSmoker == "Yes" else 0

    cigsPerDay = st.number_input("Cigarettes/day", 0, 50, 0)

with col2:
    BPMeds = st.selectbox("BP Medication", ["No", "Yes"])
    BPMeds = 1 if BPMeds == "Yes" else 0

    prevalentStroke = st.selectbox("Stroke History", ["No", "Yes"])
    prevalentStroke = 1 if prevalentStroke == "Yes" else 0

    prevalentHyp = st.selectbox("Hypertension", ["No", "Yes"])
    prevalentHyp = 1 if prevalentHyp == "Yes" else 0

    diabetes = st.selectbox("Diabetes", ["No", "Yes"])
    diabetes = 1 if diabetes == "Yes" else 0

st.divider()

# -------------------- CLINICAL DATA --------------------
st.subheader("🩺 Clinical Measurements")

col3, col4 = st.columns(2)

with col3:
    totChol = st.number_input("Cholesterol", 100, 400, 200)
    sysBP = st.number_input("Systolic BP", 80, 200, 120)
    diaBP = st.number_input("Diastolic BP", 50, 130, 80)

with col4:
    BMI = st.number_input("BMI", 15.0, 50.0, 25.0)
    heartRate = st.number_input("Heart Rate", 40, 120, 70)
    glucose = st.number_input("Glucose", 70, 300, 100)

# -------------------- VALIDATION --------------------
if sysBP < diaBP:
    st.warning("⚠️ Systolic BP should be higher than Diastolic BP")

st.divider()

# -------------------- PREDICTION --------------------
if st.button("🔍 Predict CHD Risk", use_container_width=True):

    # Create input dictionary
    input_dict = {
        'male': male,
        'age': age,
        'currentSmoker': currentSmoker,
        'cigsPerDay': cigsPerDay,
        'BPMeds': BPMeds,
        'prevalentStroke': prevalentStroke,
        'prevalentHyp': prevalentHyp,
        'diabetes': diabetes,
        'totChol': totChol,
        'sysBP': sysBP,
        'diaBP': diaBP,
        'BMI': BMI,
        'heartRate': heartRate,
        'glucose': glucose
    }

    # Arrange input in correct feature order
    input_data = np.array([[input_dict[feature] for feature in features]])

    # Predict
    prediction = model.predict(input_data)

    st.divider()

    # Output
    if prediction[0] == 1:
        st.error("🚨 High Risk of Coronary Heart Disease")
    else:
        st.success("✅ Low Risk of Coronary Heart Disease")
