import streamlit as st
import mediapipe as mp
import cv2 as cv
import numpy as np
from PIL import Image

image_1 = Image.open('face_1.jpg')
image_2 = Image.open('face_2.jpg')
image_3 = Image.open('face_3.jpg')
image_4 = Image.open('face_4.jpg')

col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.title("Face cropping")
    st.image(image_1)
    st.image(image_2)
    st.image(image_3)
    st.image(image_4)

with col3:
    st.write("")


