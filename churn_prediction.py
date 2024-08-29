import streamlit as st
import pickle
import pandas as pd

# Load your trained model
loaded_model = pd.read_pickle("trained_model.sav")

# Streamlit application
st.title("Expresso Churn Prediction")

# Create input fields for columns
feature1 = st.number_input('REVENUE')
feature2 = st.number_input('FREQUENCY_RECH')
feature3 = st.number_input('MONTANT')
feature4 = st.number_input('CHURN')

# Adding a button to make predictions
if st.button('Predict'):
    input_data = [[feature1, feature2, feature3, feature4]] 
    prediction = loaded_model.predict(input_data)
    st.write(f"The predicted churn probability is: {prediction[0]}")











