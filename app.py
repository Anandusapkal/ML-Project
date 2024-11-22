import streamlit as st
import pandas as pd
import joblib

# Custom CSS to inject
custom_css = """
<style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .app-header {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Load the trained model
model = joblib.load('model.pkl')

# Streamlit app title
st.image("header_image.png", use_column_width=True)  # Add your path to a header image
st.title("Brain Stroke Prediction App")

# Decorative header
st.markdown('<div class="app-header"><h1 class="big-font">Stroke Prediction Dashboard</h1></div>', unsafe_allow_html=True)

# User inputs with some styling
gender = st.radio("Gender", ('Male', 'Female'))
age = st.number_input("Age (in years)", min_value=0, max_value=120, value=30)
hypertension = st.radio("Hypertension", ('No', 'Yes'))
heart_disease = st.radio("Heart Disease", ('No', 'Yes'))
ever_married = st.radio("Ever Married", ('No', 'Yes'))
work_type = st.selectbox("Work Type", ['Private', 'Self-employed', 'Government Job', 'Children', 'Never worked'])
Residence_type = st.radio("Residence Type", ('Urban', 'Rural'))
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, max_value=500.0, value=100.0)
smoking_status = st.selectbox("Smoking Status", ['never smoked', 'formerly smoked', 'smokes', 'Unknown'])

# Data processing and prediction
# [Same as your existing code]

# Display the result with larger and bold text
prediction_display = "### Prediction: **High Risk of Stroke**" if prediction[0] == 1 else "### Prediction: **Low Risk of Stroke**"
st.markdown(prediction_display, unsafe_allow_html=True)
