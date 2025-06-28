import pybullet as p
import time

def move_forward(robot_id, duration=1.0, speed=2.0):
    wheel_joints = [2, 3, 4, 5]  # Husky wheels
    for joint in wheel_joints:
        p.setJointMotorControl2(robot_id, joint, p.VELOCITY_CONTROL, targetVelocity=speed)
    steps = int(duration / 0.01)
    for _ in range(steps):
        p.stepSimulation()
        time.sleep(0.01)

def stop(robot_id):
    wheel_joints = [2, 3, 4, 5]
    for joint in wheel_joints:
        p.setJointMotorControl2(robot_id, joint, p.VELOCITY_CONTROL, targetVelocity=0)
