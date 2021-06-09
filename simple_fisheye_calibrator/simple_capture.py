#! /usr/bin/env python

import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    cv2.imshow('Capture Image', frame)

    key_input = cv2.waitKey(1) & 0xFF

    if key_input == ord('q'):
        break

    if key_input == ord('c'):
        cv2.imwrite('fisheye_test.jpg', frame)

cap.release()
cv2.destroyAllWindows()