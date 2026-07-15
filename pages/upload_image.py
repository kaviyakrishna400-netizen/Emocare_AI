import streamlit as st
import cv2
import numpy as np

from utils.face_detector import detect_faces
from utils.emotion_predictor import predict_emotion
from utils.db import save_detection


def show():

    st.title("🖼 Upload Image")

    st.info("Upload an image for emotion detection.")

    uploaded_file = st.file_uploader(
        "Choose an Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

        image = cv2.imdecode(file_bytes, 1)

        faces = detect_faces(image)

        for (x, y, w, h) in faces:

            face = image[y:y+h, x:x+w]

            emotion, confidence = predict_emotion(face)

            save_detection(emotion, confidence)

            cv2.rectangle(
                image,
                (x, y),
                (x+w, y+h),
                (0,255,0),
                2
            )

            cv2.putText(
                image,
                f"{emotion} ({confidence:.1f}%)",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,0),
                2
            )

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        st.image(image, use_container_width=True)

        if len(faces) == 0:
            st.warning("No face detected.")
        else:
            st.success("Emotion Detection Completed!")