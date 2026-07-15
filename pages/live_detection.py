import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av
import cv2
import time

from utils.db import save_detection
from utils.face_detector import detect_faces
from utils.emotion_predictor import predict_emotion


class VideoProcessor(VideoProcessorBase):

    def __init__(self):
        self.last_saved = 0

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        faces = detect_faces(img)

        for (x, y, w, h) in faces:

            face = img[y:y+h, x:x+w]

            emotion, confidence = predict_emotion(face)

            # Save once every 3 seconds
            current_time = time.time()

            if current_time - self.last_saved > 3:
                save_detection(emotion, confidence)
                self.last_saved = current_time

            # Draw rectangle around face
            cv2.rectangle(
                img,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Display emotion and confidence
            text = f"{emotion} ({confidence:.1f}%)"

            cv2.putText(
                img,
                text,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


def show():

    st.title("🧠 AI Emotion Detection")

    st.write("Click **START** to begin real-time emotion detection.")

    webrtc_streamer(
        key="emotion",
        video_processor_factory=VideoProcessor,
        media_stream_constraints={
            "video": True,
            "audio": False
        }
    )