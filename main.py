from src.simulation import setup_scene
from src.camera import set_camera_view, capture_image
from src.perception import detect_object
from config import CAMERA_POSITIONS, CONFIDENCE_THRESHOLD

def main():
    setup_scene()
    for pos in CAMERA_POSITIONS:
        set_camera_view(pos)
        rgb_img = capture_image()
        confidence = detect_object(rgb_img)
        print(f"[View @ {pos}] Confidence: {confidence:.2f}")
        if confidence >= CONFIDENCE_THRESHOLD:
            print("✅ Object recognized with high confidence.")
            break
    else:
        print("❌ Could not confidently identify object after all views.")

if __name__ == "__main__":
    main()
