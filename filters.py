"""
Contains all image filter functions used in the project.
"""
import cv2
import numpy as np

# Filter-1
def original(frame):
    return frame

# Filter-2
def black_white(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Filter-3
def sepia(frame):
    kernel = np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168],
        [0.393, 0.769, 0.189]
    ])
    sepia_img = cv2.transform(frame, kernel)
    sepia_img = np.clip(sepia_img, 0, 255)
    return sepia_img.astype(np.uint8)

# Filter-4
def sketch(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted = 255 - gray

    # Blur the inverted image
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

    # Invert the blurred image
    inverted_blur = 255 - blurred

    # Create sketch effect
    sketch_img = cv2.divide(gray, inverted_blur, scale=256.0)

    # Convert back to BGR
    return cv2.cvtColor(sketch_img, cv2.COLOR_GRAY2BGR)

# Filter-5
def cartoon(frame):
    # Convert image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Detect edges
    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    # Smooth the colors
    color = cv2.bilateralFilter(frame, 9, 250, 250)

    # Combine edges with color image
    cartoon_img = cv2.bitwise_and(color, color, mask=edges)
    return cartoon_img

# Filter-6
def vintage(frame):
    # Split the image into B, G, R channels
    blue, green, red = cv2.split(frame)

    # Slightly reduce blue and increase red
    blue = cv2.addWeighted(blue, 0.8, blue, 0, 0)
    red = cv2.addWeighted(red, 1.2, red, 0, 20)

    # Merge channels back
    vintage_img = cv2.merge((blue, green, red))
    return vintage_img

# Filter-7
def warm(frame):
    warm = frame.copy()

    # Increase Red
    warm[:, :, 2] = cv2.add(warm[:, :, 2], 30)

    # Increase Green slightly
    warm[:, :, 1] = cv2.add(warm[:, :, 1], 10)
    return warm

# Filter-8
def cool(frame):
    cool = frame.copy()

    # Increase Blue
    cool[:, :, 0] = cv2.add(cool[:, :, 0], 30)

    # Reduce Red
    cool[:, :, 2] = cv2.subtract(cool[:, :, 2], 20)

    return cool

# Bonus Feature

def cinematic(frame):
    img = frame.copy()

    # Increase contrast
    img = cv2.convertScaleAbs(img, alpha=1.2, beta=10)

    # Enhance red channel
    img[:, :, 2] = cv2.add(img[:, :, 2], 15)

    # Slightly reduce blue
    img[:, :, 0] = cv2.subtract(img[:, :, 0], 10)
    return img
