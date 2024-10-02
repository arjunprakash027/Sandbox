import cv2
import streamlit as st

st.title("Webcam Live Feed")
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

if st.button('Start'):
    while True:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

