import streamlit as st
st.write("Hello, let's learn how to build a streamlit app together")

st.title ("this is the app title")
st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this is the subheader")
st.caption("this the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

#displaying audio ,video and image with streamlit
st.subheader("image")
st.image("WIN_20240611_15_06_57_Pro.jpg")
st.subheader("Audio")
#st.audio("Audio.mp3")
st.subheader("video")
st.video("WIN_20240611_15_07_47_Pro.mp4")


#imput widget
st.checkbox('yes','no')
st.button('click')
st.radio('pick your gender',['male','Female'])
st.selectbox('pick your gender',['male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

import matplotlib.pyplot as plt
import numpy as np
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

import pandas as pd
df= pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)