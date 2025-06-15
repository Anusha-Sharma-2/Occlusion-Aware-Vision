from config import CAMERA_POSITIONS

def next_best_view(current_index):
    next_index = current_index + 1
    if next_index < len(CAMERA_POSITIONS):
        return CAMERA_POSITIONS[next_index]
    else:
        return None
