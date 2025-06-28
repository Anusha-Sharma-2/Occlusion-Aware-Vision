from config import CAMERA_POSITIONS
import numpy as np

def next_best_view(current_index):
    next_index = current_index + 1
    if next_index < len(CAMERA_POSITIONS):
        return CAMERA_POSITIONS[next_index]
    else:
        return None

def generate_camera_positions(radius=0.2, height=1.0, steps=16):
    """
    Orbit the camera around the object in a circle
    """
    angles = np.linspace(0, 2 * np.pi, steps, endpoint=False)
    positions = []

    for theta in angles:
        x = radius * np.cos(theta) + 0.5  # center around (0.5, 0)
        y = radius * np.sin(theta)
        z = height
        positions.append([x, y, z])

    return positions

