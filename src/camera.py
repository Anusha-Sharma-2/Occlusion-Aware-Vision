import pybullet as p
import numpy as np

def capture_robot_camera(robot_id):
    pos, orn = p.getBasePositionAndOrientation(robot_id)
    pos = list(pos)
    target = [pos[0] + 0.5, pos[1], pos[2] + 0.2]  # look ahead

    view_matrix = p.computeViewMatrix(pos, target, [0, 0, 1])
    proj_matrix = p.computeProjectionMatrixFOV(60, 1.0, 0.1, 3.1)

    _, _, rgb, _, _ = p.getCameraImage(320, 240, view_matrix, proj_matrix)
    rgb_image = np.reshape(rgb, (240, 320, 4))[:, :, :3].astype(np.uint8)
    return rgb_image
