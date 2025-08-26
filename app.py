import streamlit as st
from PIL import Image

st.title("Mi primera app!!")
image = Image.open('Logo-nuevo-Simac-300x135.png')
st.image(image, caption= 'Logo')
