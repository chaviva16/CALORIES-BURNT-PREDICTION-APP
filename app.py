# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 03:06:09 2024

@author: user
"""
import streamlit as st
import pickle
import pandas as pd

movies = pd.read_pickle("movies_list.pkl")
similarity = pd.read_pickle("similarity.pkl")
movies_list = movies["title"].values

st.header("Movie Recommender System")
select_value = st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index = movies[movies.title == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie


if st.button("Show Recommendations"):
    movie_name = recommend(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])
    

