import cv2
import numpy as np
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import model # this is model.py, the file of ML functions

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

click(600, 483)

# Create a VideoCapture object. This object will be used to capture the video from your screen:
cap = cv2.VideoCapture(0)

# Create a VideoWriter object. This object will be used to write the recorded video to a file:
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1920, 1080)) to store a video I think

# Start a loop to capture and write the video:
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

# Release the VideoCapture and VideoWriter objects:
cap.release()
#out.release()