import pybullet as p
import pybullet_data
import time

def setup_scene():
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())

    # Base environment
    p.loadURDF("plane.urdf")
    p.loadURDF("table/table.urdf", [0.5, 0, 0])
    target_pos = [0.55, 0.0, 0.85]
    p.loadURDF("random_urdfs/000/000.urdf", target_pos)

    # Maze wall layout around the object
    wall_scale = 0.1
    wall_z = 0.85
    wall_positions = [
        [0.45, 0.1], [0.55, 0.1], [0.65, 0.1],
        [0.45, 0.0],           [0.65, 0.0],
        [0.45, -0.1], [0.55, -0.1], [0.65, -0.1],
    ]

    for pos in wall_positions:
        x, y = pos
        p.loadURDF("cube.urdf", [x, y, wall_z], globalScaling=wall_scale)

    p.setGravity(0, 0, -9.8)
    time.sleep(1)
