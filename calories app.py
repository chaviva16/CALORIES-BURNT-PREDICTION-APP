import streamlit as st
import numpy as np
import pickle

with open('C:/Users/USER/OneDrive/Desktop/Gomycode/pipeline.pkl','rb') as f:
    pipeline_saved = pickle.load(f)

# Title of the app
st.title('Calorie Burn Prediction App')

# Collect user input
gender = st.selectbox('Select your gender', ['Male', 'Female'])
age = st.number_input('Enter your age', min_value=0, max_value=100, value=25)
height = st.number_input('Enter your height (in cm)', min_value=100.0, max_value=250.0, value=170.0)
weight = st.number_input('Enter your weight (in kg)', min_value=0.0, max_value=200.0, value=70.0)
duration = st.number_input('Enter the duration of exercise (in minutes)', min_value=0, max_value=300, value=30)
heart_rate = st.number_input('Enter your heart rate (in bpm)', min_value=30, max_value=200, value=120)
body_temp = st.number_input('Enter your body temperature (in Celsius)', min_value=35.0, max_value=42.0, value=36.5)

# Encode gender input for prediction
gender_encoded = 0 if gender == 'Male' else 1

# Prepare the input for prediction
input_data = np.array([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]])

# Make prediction
if st.button('Predict'):
    prediction = pipeline_saved.predict(input_data)
    st.write(f'Estimated calories burned: {prediction[0]:.2f}')