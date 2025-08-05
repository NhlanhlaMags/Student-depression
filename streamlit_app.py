import streamlit as st
import pandas as pd
import joblib

# Load trained model pipeline
model = joblib.load("model.pkl")  # Make sure model.pkl is in the same directory or provide full path

st.title("Student Mental Health Risk Prediction")

st.markdown("Fill in the details below to get a prediction.")

# Input fields
id_ = st.text_input("ID")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=10, max_value=100, value=20)
city = st.text_input("City")
profession = st.text_input("Profession")
academic_pressure = st.selectbox("Academic Pressure", ["Low", "Moderate", "High"])
work_pressure = st.selectbox("Work Pressure", ["Low", "Moderate", "High"])
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
study_satisfaction = st.slider("Study Satisfaction (1-10)", 1, 10, 5)
job_satisfaction = st.slider("Job Satisfaction (1-10)", 1, 10, 5)
sleep_duration = st.selectbox("Sleep Duration", ["< 5 hours", "5-6 hours", "6-8 hours", "> 8 hours"])
dietary_habits = st.selectbox("Dietary Habits", ["Healthy", "Average", "Poor"])
degree = st.text_input("Degree")
suicidal_thoughts = st.selectbox("Have you ever had suicidal thoughts?", ["Yes", "No"])
study_hours = st.number_input("Work/Study Hours per day", min_value=0, max_value=24, step=1)
financial_stress = st.selectbox("Financial Stress", ["Yes", "No"])
family_history = st.selectbox("Family History of Mental Illness", ["Yes", "No"])

# Create input DataFrame
input_data = pd.DataFrame({
    'id': [id_],
    'Gender': [gender],
    'Age': [age],
    'City': [city],
    'Profession': [profession],
    'Academic Pressure': [academic_pressure],
    'Work Pressure': [work_pressure],
    'CGPA': [cgpa],
    'Study Satisfaction': [study_satisfaction],
    'Job Satisfaction': [job_satisfaction],
    'Sleep Duration': [sleep_duration],
    'Dietary Habits': [dietary_habits],
    'Degree': [degree],
    'Have you ever had suicidal thoughts ?': [suicidal_thoughts],
    'Work/Study Hours': [study_hours],
    'Financial Stress': [financial_stress],
    'Family History of Mental Illness': [family_history]
})

# Predict button
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        st.success(f"Prediction: {prediction[0]}")
    except Exception as e:
        st.error(f"Error: {e}")
