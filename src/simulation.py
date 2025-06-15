import pybullet as p
import pybullet_data
import time

def setup_scene():
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.loadURDF("plane.urdf")
    p.loadURDF("table/table.urdf", [0.5, 0, 0])
    p.loadURDF("random_urdfs/000/000.urdf", [0.6, 0, 0.8])  # target object
    p.loadURDF("cube_small.urdf", [0.55, 0.05, 0.85])        # occluder
    p.setGravity(0, 0, -9.8)
    time.sleep(1)
