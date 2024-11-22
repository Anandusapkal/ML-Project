import streamlit as st
import pandas as pd
import joblib

# URL of the background image
background_image_url = "https://example.com/path/to/your/background_image.jpg"  # Replace with valid background image URL
header_image_url = "https://example.com/path/to/your/header_image.png"  # Replace with valid header image URL

# Custom CSS to inject background image and animations
custom_css = f"""
<style>
    .stApp {{
        background-image: url('{background_image_url}');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 100vh;
        color: white;
    }}
    .big-font {{
        font-size:30px !important;
        font-weight: bold;
    }}
    .app-header {{
        background-color: rgba(0, 0, 0, 0.7);
        padding: 10px;
        border-radius: 10px;
        animation: fadeIn 2s;
    }}
    @keyframes fadeIn {{
        from {{
            opacity: 0;
        }}
        to {{
            opacity: 1;
        }}
    }}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Load the trained model
model = joblib.load('model.pkl')

# Streamlit app title
st.image(header_image_url, use_column_width=True)  # Display header image
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

# Encode categorical inputs (same as your existing code)
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

# Display the result with larger and bold text
prediction_display = "### Prediction: **High Risk of Stroke**" if prediction[0] == 1 else "### Prediction: **Low Risk of Stroke**"
st.markdown(prediction_display, unsafe_allow_html=True)
