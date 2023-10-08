import cv2
import numpy as np
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from model import Model # this is model.py, the file of ML functions
import torch

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#click(600, 483)
def main():
    # Create the model
    model = Model()

    # Capture a frame from the game window
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Press m to catch each card on the frame
    if cv2.waitKey(1) & 0xFF == ord('m'):
        # Predict the bounding boxes of the cards in the frame
        predictions = model.predict(frame)

        # Draw the bounding boxes on the frame
        for prediction in predictions:
            cv2.rectangle(frame, (prediction[0], prediction[1]), (prediction[2], prediction[3]), (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Game Window", frame)

    # Repeat until the user presses q to quit
    while cv2.waitKey(1) != ord('q'):
        ret, frame = cap.read()

        # Press m to catch each card on the frame
        if cv2.waitKey(1) & 0xFF == ord('m'):
            # Predict the bounding boxes of the cards in the frame
            predictions = model.predict(frame)

            # Draw the bounding boxes on the frame
            for prediction in predictions:
                cv2.rectangle(frame, (prediction[0], prediction[1]), (prediction[2], prediction[3]), (0, 0, 255), 2)

        # Display the frame
        cv2.imshow("Game Window", frame)

    # Release the VideoCapture object
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
"""    
# Load the model
model = torch.load("/path/to/trained/model.pt")

# Create a VideoCapture object. This object will be used to capture the video from your screen:
cap = cv2.VideoCapture(0)

# Create a VideoWriter object. This object will be used to write the recorded video to a file:
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1920, 1080)) to store a video I think

# Start a loop to capture and write the video:
# What if I have start boolean that represents initiative phase?
# Look for the Confirm button to check if it is the starting phase right now
# refer to Confirm.png in assets folder
start = True
while True:
    # Capture the virtual webcam
    ret, frame = cap.read()
    if not ret:
        break

    #out.write(frame) to write the output.mp4 video

    cv2.imshow('Gaming Window', frame)
    # if the user press q on the keyboard, break.
    pressed = cv2.waitKey(1)
    if pressed == ord('q'):
        break
    elif pressed == ord('w'):
        click(600, 483)
    elif pressed == ord('s'):
        cards = model.scan(frame)
        # Do something with the recognized cards
    elif pressed == ord('m'):
        # Predict the bounding boxes of the cards in the frame
        predictions = model.predict(frame)

        # Draw the bounding boxes on the frame
        for prediction in predictions:
            cv2.rectangle(frame, (prediction[0], prediction[1]), (prediction[2], prediction[3]), (0, 0, 255), 2)
        cv2.waitKey(1)

# Release the VideoCapture and VideoWriter objects:
cap.release()
#out.release()"""