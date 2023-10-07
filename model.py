# This file would contain the code for the machine learning model that is used by the agent.

import cv2
import numpy as np

def scan(image):
    """Scans the given image and returns a list of the recognized cards."""

    # Preprocess the image
    image = cv2.resize(image, (224, 224))
    image = np.array(image, dtype=np.float32) / 255.0

    # Make a prediction
    prediction = predict(image)

    # Return the predicted card classes
    return prediction.argmax()

def predict(image):
    """Predicts the scanned pixel's result and return the prediction"""
    return
