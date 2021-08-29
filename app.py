import streamlit as st
import cv2
 
st.title("Webcam Application")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(0)

while run:
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # result= detect_faces_live(frame)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')
