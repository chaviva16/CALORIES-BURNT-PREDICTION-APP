import streamlit as st
import numpy as np
import pickle
import pandas as pd
import requests
import os

with open('pipeline.pkl','rb') as f:
    pipeline_saved = pickle.load(f)

# Title of the app
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


# Function to download a file from a URL
def download_file(url, output_filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_filename, 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

# Streamlit app layout
st.title("Download Files from Google Drive")

# Google Drive file IDs
file_ids = {
    "pipeline.pkl": "1S9kdM8lwRmveLURHayyAFh712AUVWOQp",
    "calories_app.py": "1wuGnKYcMwfVDNeegcyYvxcZRgIVw9Vxw",  # Update with correct ID
    "CALORIES BURNT PREDICTION.ipynb": "1h9RjYzDLP8DulrqAh5npOfyYkBFUAL6j"    # Update with correct ID
}

# Generate download URLs
file_urls = {name: f"https://drive.google.com/uc?id={file_id}" for name, file_id in file_ids.items()}

# Create a download button for each file
for filename, url in file_urls.items():
    if st.button(f"Download {filename}"):
        success = download_file(url, filename)
        if success:
            st.success(f"{filename} downloaded successfully!")
        else:
            st.error(f"Failed to download {filename}.")

import os

def split_file(file_path, chunk_size):
    with open(file_path, 'rb') as f:
        chunk_num = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            with open(f'{file_path}.{chunk_num:03}', 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunk_num += 1

split_file('large_file.pkl', 50*1024*1024)  # 50MB chunks



