import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Custom CSS to set the background image and add animations
custom_css = """
<style>
    body {
        background-image: url('ML img.jpg');  /* Path to your background image */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #fff;  /* Change text color for better visibility */
    }
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
    }
    .app-header {
        background-color: rgba(0, 0, 0, 0.5);  /* Semi-transparent background */
        padding: 20px;
        border-radius: 10px;
        animation: fadeIn 1s;  /* Animation for header */
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .result {
        background-color: rgba(255, 255, 255, 0.7);  /* Semi-transparent result background */
        padding: 15px;
        border-radius: 10px;
        animation: slideIn 0.5s;  /* Animation for results */
    }
    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Streamlit app title
st.image("ML img2.png", use_column_width=True)  # Update with your header image
st.title("Brain Stroke Prediction App")

# Decorative header
st.markdown('<div class="app-header"><h1 class="big-font">Stroke Prediction Dashboard</h1></div>', unsafe_allow_html=True)

# User inputs
gender = st.radio("Gender", ('Male', 'Female'))
age = st.number_input("Age (in years)", min_value=0, max_value=120, value=30)
hypertension = st.radio("Hypertension", ('No', 'Yes'))
heart_disease = st.radio("Heart Disease", ('No', 'Yes'))
ever_married = st.radio("Ever Married", ('No', 'Yes'))
work_type = st.selectbox("Work Type", ['Private', 'Self-employed', 'Government Job', 'Children', 'Never worked'])
Residence_type = st.radio("Residence Type", ('Urban', 'Rural'))
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, max_value=500.0, value=100.0)
smoking_status = st.selectbox("Smoking Status", ['never smoked', 'formerly smoked', 'smokes', 'Unknown'])

# Encode categorical inputs
# [Same encoding logic as your existing code]

# Create a DataFrame from user input
user_input = pd.DataFrame({
    'gender': [gender],
    'age': [age],
    'hypertension': [hypertension],
    'heart_disease': [heart_disease],
    'ever_married': [ever_married],
    'work_type': [work_type],
    'Residence_type': [Residence_type],
    'avg_glucose_level': [avg_glucose_level],
    'smoking_status': [smoking_status]
})

# Make the prediction
prediction = model.predict(user_input)

# Display the result with animations
result_display = "### Prediction: **High Risk of Stroke**" if prediction[0] == 1 else "### Prediction: **Low Risk of Stroke**"
st.markdown(f'<div class="result">{result_display}</div>', unsafe_allow_html=True)
