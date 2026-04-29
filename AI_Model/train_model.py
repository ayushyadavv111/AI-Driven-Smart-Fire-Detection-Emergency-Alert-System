import cv2
import numpy as np
import serial
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)

fire_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for better detection of small flames
    frame = cv2.resize(frame, (640, 480))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 🔥 Improved fire color range (detects matchstick better)
    lower = np.array([0, 100, 100])
    upper = np.array([40, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    # Remove noise
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.GaussianBlur(mask, (9,9), 0)

    # Count fire pixels
    fire_pixels = np.sum(mask > 0)

    # 🔥 Lower threshold for small flames
    if fire_pixels > 8000:
        fire_count += 1
    else:
        fire_count = 0

    # Stability check
    if fire_count > 3:
        print("🔥 FIRE DETECTED")
        arduino.write(b'1')
    else:
        arduino.write(b'0')

    # Show output
    cv2.imshow("Camera", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
