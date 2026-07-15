import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("models/emotion_model.h5")

# Emotion labels (must match your training folders)
emotion_labels = [
    "Angry",
    "Disgust",
    "Fear",
    "Happy",
    "Neutral",
    "Sad",
    "Surprise"
]

def predict_emotion(face):

    # Convert to grayscale
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    # Resize to model input size
    gray = cv2.resize(gray, (48, 48))

    # Normalize
    gray = gray.astype("float32") / 255.0

    # Reshape
    gray = np.expand_dims(gray, axis=-1)
    gray = np.expand_dims(gray, axis=0)

    # Predict
    prediction = model.predict(gray, verbose=0)

    emotion = emotion_labels[np.argmax(prediction)]
    confidence = float(np.max(prediction) * 100)

    return emotion, confidence