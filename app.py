# Streamlit app for Brain Stroke Prediction
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Streamlit app title
st.title("Brain Stroke Prediction App")

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
gender = 1 if gender == 'Male' else 0
hypertension = 1 if hypertension == 'Yes' else 0
heart_disease = 1 if heart_disease == 'Yes' else 0
ever_married = 1 if ever_married == 'Yes' else 0
work_type_mapping = {'Private': 0, 'Self-employed': 1, 'Government Job': 2, 'Children': 3, 'Never worked': 4}
work_type = work_type_mapping[work_type]
Residence_type = 1 if Residence_type == 'Urban' else 0
smoking_status_mapping = {'never smoked': 0, 'formerly smoked': 1, 'smokes': 2, 'Unknown': 3}
smoking_status = smoking_status_mapping[smoking_status]

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

# Display the result
if prediction[0] == 1:
    st.write("### Prediction: **High Risk of Stroke**")
else:
    st.write("### Prediction: **Low Risk of Stroke**")
