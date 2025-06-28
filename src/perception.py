import numpy as np
import cv2

def detect_object(image):
    """
    Simulate a confidence score based on brightness (occlusion proxy).
    Replace with YOLO later.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    mean_pixel = np.mean(gray)
    confidence = min(1.0, mean_pixel / 255.0 + np.random.normal(0, 0.05))
    return max(0.0, confidence)