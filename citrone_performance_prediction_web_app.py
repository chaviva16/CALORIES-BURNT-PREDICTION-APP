# -*- coding: utf-8 -*-
"""
Created on Tue May  2 22:55:26 2023

@author: TEMITOPE
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd

# #loading the saved model
#loaded_model = pickle.load(open("trained_model.sav", "rb"))
loaded_model = pd.read_pickle("trained_model.sav")


def performance_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array so the model will understand I am making prediction for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "This student is not eligible for intermediate class"
    else:
        return "This student is eligible for intermediate class"


def main():

    # giving the app a title
    st.title("Citrone performance Web App")

    # getting the input data from user

    Quiz_Summary = st.text_input("Quiz Summary score")
    Assignment_Summary = st.text_input("Assignment Summary score")
    Grade_Point_Average = st.text_input("Learner's Grade point Average score")
    Age = st.text_input("learner's Age")
    Children = st.text_input(
        "Does learner have child/children ? 1 for Yes/0 for No")
    Completed_Nysc = st.text_input("Completed Nysc ? 1 for Yes/0 for No")
    Gender = st.text_input("Is learner's gender ? 1 for Male/0 for Female")
    # Gender_Female = st.text_input("Is learner's gender female ?")
    # Gender_Male = st.text_input("Is learner's gender male")

    # code for Prediction
    performance = ""

    # creating a button for prediction

    if st.button("Eligibility Result"):
        performance = performance_prediction(
            [Quiz_Summary, Assignment_Summary, Grade_Point_Average, Age, Children, Completed_Nysc, Gender])
        st.success(performance)


if __name__ == "__main__":
    main()
