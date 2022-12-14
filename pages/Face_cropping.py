import streamlit as st
import cv2
import mediapipe as mp
from PIL import Image

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# For static images:
faces = ['face_1.jpg','face_2.jpg','face_3.jpg','face_4.jpg']
IMAGE_FILES = st.selectbox(label = 'Select a face', options = faces, index=0)

with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.2) as face_detection:
  for idx, file in enumerate([IMAGE_FILES]):
    image = cv2.imread(file)
    # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw face detections of each face.
    if not results.detections:
        st.write('no face detected')
        continue
    annotated_image = image.copy()
    for detection in results.detections:
      st.write('Nose tip:')
      st.write(mp_face_detection.get_key_point(
          detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
      mp_drawing.draw_detection(annotated_image, detection)
    image_1 = annotated_image


col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.title("Face cropping")
    st.image(image_1)
    st.image(IMAGE_FILES)
with col3:
    st.write("")