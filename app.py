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

# Rest of your code remains the same
