"""
Project: Real-Time Instagram Style Filters
Course: AI/ML Internship - Week 4 Computer Vision Assignment

Features:
- Live Webcam Feed
- 9 Image Filters
- Keyboard Controls
- Capture & Save Images
- Welcome Message
- Date & Time Display
"""

import cv2
import filters
import os
from datetime import datetime

# -------------------------------
# Webcam Setup
# -------------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

# -------------------------------
# Create Captures Folder
# -------------------------------
if not os.path.exists("captures"):
    os.makedirs("captures")

# -------------------------------
# Variables
# -------------------------------
current_filter = 0
save_message = ""
message_time = None
start_time = datetime.now()

# -------------------------------
# Filter Names
# -------------------------------
filter_names = {
    0: "Original",
    1: "Black & White",
    2: "Sepia",
    3: "Sketch",
    4: "Cartoon",
    5: "Vintage",
    6: "Warm",
    7: "Cool",
    8: "Cinematic"
}

# -------------------------------
# Instructions
# -------------------------------
print("=" * 50)
print("        Instagram Style Filters")
print("=" * 50)
print("0 : Original")
print("1 : Black & White")
print("2 : Sepia")
print("3 : Sketch")
print("4 : Cartoon")
print("5 : Vintage")
print("6 : Warm")
print("7 : Cool")
print("8 : Cinematic")
print("C : Capture Image")
print("Q : Quit")
print("=" * 50)

# -------------------------------
# Main Loop
# -------------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # ---------------------------
    # Apply Selected Filter
    # ---------------------------
    if current_filter == 0:
        output = filters.original(frame)

    elif current_filter == 1:
        output = filters.black_white(frame)

    elif current_filter == 2:
        output = filters.sepia(frame)

    elif current_filter == 3:
        output = filters.sketch(frame)

    elif current_filter == 4:
        output = filters.cartoon(frame)

    elif current_filter == 5:
        output = filters.vintage(frame)

    elif current_filter == 6:
        output = filters.warm(frame)

    elif current_filter == 7:
        output = filters.cool(frame)

    elif current_filter == 8:
        output = filters.cinematic(frame)

    # ---------------------------
    # Project Title
    # ---------------------------
    cv2.putText(
        output,
        "Instagram Style Filters",
        (110, 30),
        cv2.FONT_HERSHEY_DUPLEX,
        0.8,
        (255, 0, 255),
        2
    )

    # ---------------------------
    # Current Filter
    # ---------------------------
    cv2.putText(
        output,
        f"Filter: {filter_names[current_filter]}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 165, 255),
        2
    )

    # ---------------------------
    # Welcome Message
    # ---------------------------
    if (datetime.now() - start_time).seconds < 3:
        cv2.putText(
            output,
            "Welcome! Press the keys to explore filters.",
            (30, 105),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

    # ---------------------------
    # Image Saved Message
    # ---------------------------
    if save_message:

        if (datetime.now() - message_time).seconds < 2:

            cv2.putText(
                output,
                save_message,
                (20, 140),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        else:
            save_message = ""

    # ---------------------------
    # Keyboard Shortcuts
    # ---------------------------
    cv2.putText(
        output,
        "0-Original  1-B&W  2-Sepia  3-Sketch",
        (20, output.shape[0] - 85),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 255, 0),
        1
    )

    cv2.putText(
        output,
        " 4-Cartoon  5-Vintage  6-Warm  7-Cool  8-Cinematic",
        (20, output.shape[0] - 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 255, 0),
        1
    )

    cv2.putText(
        output,
        "C-Capture     Q-Quit",
        (20, output.shape[0] - 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (0, 255, 255),
        1
    )

    # ---------------------------
    # Date & Time
    # ---------------------------
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    cv2.putText(
        output,
        current_time,
        (20, output.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        1
    )

    # ---------------------------
    # Show Webcam
    # ---------------------------
    cv2.imshow("AI ML Week 4 - Instagram Style Filters", output)

    # ---------------------------
    # Keyboard Input
    # ---------------------------
    key = cv2.waitKey(1) & 0xFF

    if ord('0') <= key <= ord('8'):
        current_filter = key - ord('0')

    elif key == ord('c'):

        filename = (
            filter_names[current_filter]
            + "_"
            + datetime.now().strftime("%Y%m%d_%H%M%S")
            + ".jpg"
        )

        filepath = os.path.join("captures", filename)

        cv2.imwrite(filepath, output)

        save_message = "Image Saved Successfully!"

        message_time = datetime.now()

    elif key == ord('q'):
        break

# -------------------------------
# Cleanup
# -------------------------------
cap.release()
cv2.destroyAllWindows()
