import cv2
import mediapipe as mp
import numpy as np
from collections import deque

# ================== INITIALIZATION ==================
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,
    enable_segmentation=False,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# ================== VARIABLES ==================
angle_buffer = deque(maxlen=10)   # smoothing buffer
status = "UNKNOWN"
previous_status = "UNKNOWN"
sit_stand_count = 0

# ================== FUNCTIONS ==================
def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - \
              np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180:
        angle = 360 - angle
    return angle

def get_knee_angle(landmarks, side):
    hip = landmarks[getattr(mp_pose.PoseLandmark, f"{side}_HIP").value]
    knee = landmarks[getattr(mp_pose.PoseLandmark, f"{side}_KNEE").value]
    ankle = landmarks[getattr(mp_pose.PoseLandmark, f"_]()
