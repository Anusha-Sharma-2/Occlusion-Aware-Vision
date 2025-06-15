import pybullet as p
import numpy as np

def set_camera_view(position):
    target = [0.5, 0, 0.8]
    up = [0, 0, 1]
    view_matrix = p.computeViewMatrix(position, target, up)
    proj_matrix = p.computeProjectionMatrixFOV(60, 1.0, 0.1, 3.1)
    p.getCameraImage(320, 240, view_matrix, proj_matrix)

def capture_image():
    width, height, rgb, _, _ = p.getCameraImage(320, 240)
    rgb_array = np.reshape(rgb, (height, width, 4)).astype(np.uint8)[:, :, :3]
    return rgb_array

