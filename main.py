import cv2
import numpy as np

# Create a VideoCapture object. This object will be used to capture the video from your screen:
cap = cv2.VideoCapture(0)

# Create a VideoWriter object. This object will be used to write the recorded video to a file:
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1920, 1080))

# Start a loop to capture and write the video:
while True:
    # Capture the virtual webcam
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)

    cv2.imshow('Gaming Window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and VideoWriter objects:
cap.release()
out.release()