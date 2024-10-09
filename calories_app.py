

import streamlit as st
import numpy as np
import pickle
import pandas as pd
import requests
import os
from pathlib import Path

# Function to download the file from Google Drive
def download_file_from_google_drive(file_id, destination):
    url = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

# File IDs for pipeline parts on Google Drive
file_id_part1 = "1bwCloAgIvI9B0jVt2GQIghwaGEDeU3k6"
file_id_part2 = "1byry_nBLjZeIoTVx5C0GM9k5YWmQHo81"
destination_part1 = "pipeline_part1.pkl"
destination_part2 = "pipeline_part2.pkl"

# Download the files
if download_file_from_google_drive(file_id_part1, destination_part1) and download_file_from_google_drive(file_id_part2, destination_part2):
    st.success("Model files downloaded successfully!")
else:
    st.error("Failed to download model files.")

# Load the model parts
file_path_part1 = Path(destination_part1)
file_path_part2 = Path(destination_part2)
with open(file_path_part1, 'rb') as f:
    part1 = pickle.load(f)
with open(file_path_part2, 'rb') as f:
    part2 = pickle.load(f)

# Combine the parts
pipeline_saved = np.concatenate((part1, part2))

# Rest of your Streamlit app
st.title('Calories Burnt Prediction App Using Machine Learning')

# Collect user input
gender = st.selectbox('Select your gender', ['male', 'female'])
age = st.number_input('Enter your age', min_value=0, max_value=100, value=25)
height = st.number_input('Enter your height (in cm)', min_value=100.0, max_value=250.0, value=170.0)
weight = st.number_input('Enter your weight (in kg)', min_value=0.0, max_value=200.0, value=70.0)
duration = st.number_input('Enter the duration of exercise (in minutes)', min_value=0, max_value=300, value=30)
heart_rate = st.number_input('Enter your heart rate (in bpm)', min_value=30, max_value=200, value=120)
body_temp = st.number_input('Enter your body temperature (in Celsius)', min_value=35.0, max_value=42.0, value=36.5)

# Prepare the input for prediction
input_data = pd.DataFrame({
    'Gender': [gender],
    'Age': [age],
    'Height': [height],
    'Weight': [weight],
    'Duration': [duration],
    'Heart_Rate': [heart_rate],
    'Body_Temp': [body_temp]
})

# Make prediction
if st.button('Predict'):
    try:
        prediction = pipeline_saved.predict(input_data)
        st.write(f'Estimated calories burned: {prediction[0]:.2f}')
    except Exception as e:
        st.write(f'An error occurred during prediction: {e}')



