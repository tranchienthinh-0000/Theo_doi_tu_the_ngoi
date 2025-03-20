import cv2
import mediapipe as mp
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import pygame
import os
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def calculate_angle_3d(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    ba, bc = a - b, c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.degrees(np.arccos(cosine_angle))

def draw_vietnamese_text(image, text, position, font_size, color, outline_color=(0, 0, 0)):
    img_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype("arial.ttf", font_size)
    x, y = position
    for offset_x in [-1, 0, 1]:
        for offset_y in [-1, 0, 1]:
            draw.text((x + offset_x, y + offset_y), text, font=font, fill=outline_color)
    draw.text(position, text, font=font, fill=color)
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Sử dụng Elgato Cam qua USB (chỉ số 0 hoặc 1 tùy thiết bị)
cap = cv2.VideoCapture(0)  # Thay đổi chỉ số nếu cần (0, 1, 2, ...)

if not cap.isOpened():
    print("Lỗi: Không thể kết nối với Elgato Cam. Kiểm tra kết nối USB hoặc chỉ số thiết bị.")
    exit()

ANGLE_MARGIN = 10
ALERT_ACTIVE = False
LAST_ALERT_TIME = 0
ALERT_COOLDOWN = 3
FRAME_SIZE = (1280, 720)  # Tăng kích thước khung hình từ (640, 480) lên (1280, 720)
TARGET_FPS = 15
FRAME_TIME = 1 / TARGET_FPS

TEXT_POSITIONS = {
    "neck_shoulder": (50, 50),
    "back_thigh": (50, 100),
    "knee": (50, 150),
    "posture": (50, 200)
}
COLORS = {
    "white": (255, 255, 255),
    "green": (0, 255, 0),
    "red": (0, 0, 255),
    "black": (0, 0, 0)
}

CORRECT_SOUND = r"D:\IOT_BTL\theo_doi_tu_the\tu_the_dung.mp3"
INCORRECT_SOUND = r"D:\IOT_BTL\theo_doi_tu_the\tu_the_sai.mp3"

pygame.mixer.init()

if not os.path.exists(CORRECT_SOUND) or not os.path.exists(INCORRECT_SOUND):
    print(f"Lỗi: Không tìm thấy file âm thanh {CORRECT_SOUND} hoặc {INCORRECT_SOUND}.")
    exit()

# Tạo cửa sổ và điều chỉnh kích thước hiển thị
cv2.namedWindow('Pose Detection', cv2.WINDOW_NORMAL)  # WINDOW_NORMAL cho phép thay đổi kích thước
cv2.resizeWindow('Pose Detection', 1280, 720)  # Đặt kích thước cửa sổ lớn hơn

print("Bắt đầu đọc video từ Elgato Cam...")
while cap.isOpened():
    start_time = time.time()
    ret, frame = cap.read()
    if not ret:
        print("Lỗi: Không thể đọc frame từ Elgato Cam.")
        break
    print(f"Frame shape: {frame.shape}")  # Kiểm tra kích thước khung hình

    frame = cv2.resize(frame, FRAME_SIZE)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(img_rgb)

    if result.pose_landmarks:
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        landmarks = result.pose_landmarks.landmark

        neck = [landmarks[mp_pose.PoseLandmark.NOSE.value].x,
                landmarks[mp_pose.PoseLandmark.NOSE.value].y,
                landmarks[mp_pose.PoseLandmark.NOSE.value].z]
        shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z]
        hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
               landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
               landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z]
        knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
                landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z]
        ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y,
                 landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z]

        angle_neck_shoulder = calculate_angle_3d(neck, shoulder, hip)
        angle_back_thigh = calculate_angle_3d(shoulder, hip, knee)
        angle_knee = calculate_angle_3d(hip, knee, ankle)

        frame = draw_vietnamese_text(frame, f"Góc Cổ - Vai: {int(angle_neck_shoulder)}",
                                     TEXT_POSITIONS["neck_shoulder"], 25, COLORS["white"], COLORS["black"])
        frame = draw_vietnamese_text(frame, f"Góc Lưng - Đùi: {int(angle_back_thigh)}",
                                     TEXT_POSITIONS["back_thigh"], 25, COLORS["white"], COLORS["black"])
        frame = draw_vietnamese_text(frame, f"Góc Đầu gối: {int(angle_knee)}",
                                     TEXT_POSITIONS["knee"], 25, COLORS["white"], COLORS["black"])

        is_correct_posture = (
            (100 - ANGLE_MARGIN) <= angle_back_thigh <= (125 + ANGLE_MARGIN) and
            (110 - ANGLE_MARGIN) <= angle_knee <= (135 + ANGLE_MARGIN) and
            (115 - ANGLE_MARGIN) <= angle_neck_shoulder <= (140 + ANGLE_MARGIN)
        )

        current_time = time.time()
        if is_correct_posture:
            frame = draw_vietnamese_text(frame, "Tư thế ngồi đúng", TEXT_POSITIONS["posture"],
                                         30, COLORS["green"], COLORS["black"])
            if not ALERT_ACTIVE and (current_time - LAST_ALERT_TIME) > ALERT_COOLDOWN:
                pygame.mixer.music.load(CORRECT_SOUND)
                pygame.mixer.music.play()
                globals()['ALERT_ACTIVE'] = True
                globals()['LAST_ALERT_TIME'] = current_time
        else:
            frame = draw_vietnamese_text(frame, "Tư thế ngồi sai", TEXT_POSITIONS["posture"],
                                         30, COLORS["red"], COLORS["black"])
            if not ALERT_ACTIVE and (current_time - LAST_ALERT_TIME) > ALERT_COOLDOWN:
                pygame.mixer.music.load(INCORRECT_SOUND)
                pygame.mixer.music.play()
                globals()['ALERT_ACTIVE'] = True
                globals()['LAST_ALERT_TIME'] = current_time

        if ALERT_ACTIVE and is_correct_posture != ALERT_ACTIVE:
            globals()['ALERT_ACTIVE'] = False

    cv2.imshow('Pose Detection', frame)

    elapsed_time = time.time() - start_time
    delay = max(1, int((FRAME_TIME - elapsed_time) * 1000))
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Chương trình đã dừng.")