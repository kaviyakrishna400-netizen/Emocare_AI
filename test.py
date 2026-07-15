import mediapipe as mp

print("MediaPipe imported from:")
print(mp.__file__)

print("\nVersion:")
print(mp.__version__)

print("\nHas solutions?", hasattr(mp, "solutions"))