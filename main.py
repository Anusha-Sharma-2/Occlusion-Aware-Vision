from src.simulation import setup_scene
from src.camera import capture_robot_camera
from src.perception import detect_object
from src.controls import move_forward, stop
from config import CONFIDENCE_THRESHOLD

import cv2
import os

def main():
    robot_id = setup_scene()
    os.makedirs("output", exist_ok=True)

    confidence_log = []

    for i in range(30):  # loop through motion + capture steps
        rgb_img = capture_robot_camera(robot_id)
        confidence = detect_object(rgb_img)
        confidence_log.append(confidence)

        print(f"[Step {i}] Confidence: {confidence:.2f}")
        img_path = f"output/view_{i}_conf_{confidence:.2f}.png"
        cv2.imwrite(img_path, cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR))

        if confidence >= CONFIDENCE_THRESHOLD:
            print("✅ Object found with high confidence!")
            break

        move_forward(robot_id, duration=0.5)

    stop(robot_id)

if __name__ == "__main__":
    main()
