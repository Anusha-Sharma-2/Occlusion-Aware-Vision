from src.simulation import setup_scene
from src.camera import set_camera_view, capture_image
from src.perception import detect_object
from src.planner import generate_camera_positions
from config import CONFIDENCE_THRESHOLD

import matplotlib.pyplot as plt
import os
import cv2

def main():
    setup_scene()
    os.makedirs("output", exist_ok=True)

    # Get smarter viewpoints (orbit camera)
    camera_positions = generate_camera_positions(radius=1.0, height=1.0, steps=8)

    confidences = []

    for i, pos in enumerate(camera_positions):
        set_camera_view(pos)
        rgb_img = capture_image()
        confidence = detect_object(rgb_img)
        confidences.append(confidence)
        print(f"[View {i} @ {pos}] Confidence: {confidence:.2f}")

        # Save image
        img_path = f"output/view_{i}_conf_{confidence:.2f}.png"
        cv2.imwrite(img_path, cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR))

        if confidence >= CONFIDENCE_THRESHOLD:
            print("Object recognized with high confidence.")
            break
    else:
        print("Could not confidently identify object after all views.")

    # Plot confidence trend
    plt.plot(range(len(confidences)), confidences, marker='o')
    plt.xlabel("View Index")
    plt.ylabel("Confidence")
    plt.title("Confidence vs Viewpoint")
    plt.grid(True)
    plt.savefig("output/confidence_plot.png")
    plt.show()

if __name__ == "__main__":
    main()
