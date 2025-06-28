import pybullet as p
import pybullet_data
import time

def setup_scene():
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.loadURDF("plane.urdf")

    # Load robot at open corner
    robot_start_pos = [0.5, 0.5, 0.1]
    robot_id = p.loadURDF("husky/husky.urdf", robot_start_pos, useFixedBase=False)

    # Target at far corner (hidden)
    p.loadURDF("random_urdfs/000/000.urdf", [4.5, 4.5, 0.05])

    # Maze: place large freestanding blocks (0.5m scale)
    wall_z = 0.1
    wall_scale = 0.5

    obstacle_positions = [
        [1.5, 0.5], [2.5, 0.5], [3.5, 0.5],
        [1.0, 1.5], [2.0, 1.5], [4.0, 1.5],
        [1.5, 2.5], [3.0, 2.5], [4.0, 2.5],
        [0.5, 3.5], [2.5, 3.5], [3.5, 3.5],
        [1.5, 4.5], [3.0, 4.5]
    ]

    for x, y in obstacle_positions:
        p.loadURDF("cube.urdf", [x, y, wall_z], globalScaling=wall_scale)

    p.setGravity(0, 0, -9.8)
    time.sleep(1)
    return robot_id
