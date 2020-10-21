import cv2
import numpy as np
import dlib
from math import hypot



# Loading camera and image
cap = cv2.VideoCapture(0)
nose_img = cv2.imread('cat_nose1.png')
ret, frame = cap.read()

rows, cols, _ = frame.shape
cat_mask = np.zeros((rows, cols), np.uint8)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Face detector

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(frame)
    for face in faces:
        landmarks = predictor(frame_gray, face)
        # Nose Coordinates
        nose_top = (landmarks.part(29).x, landmarks.part(29).y)
        nose_center = (landmarks.part(30).x, landmarks.part(30).y)
        nose_left = (landmarks.part(31).x, landmarks.part(31).y)
        nose_right = (landmarks.part(35).x, landmarks.part(35).y)

        nose_width = int(hypot(nose_left[0] - nose_right[0],
                               nose_left[1] - nose_right[1])*5)

        nose_height = int(nose_width * 0.75)

        top_left = (int(nose_center[0] - nose_width / 2),
                    int(nose_center[1] - nose_height / 2))
        bottom_right = (int(nose_center[0] + nose_width / 2),
                        int(nose_center[1] + nose_height / 2))

        cat_nose = cv2.resize(nose_img, (nose_width, nose_height))
        cat_nose_gray = cv2.cvtColor(cat_nose, cv2.COLOR_BGR2GRAY)
        _, cat_mask = cv2.threshold(cat_nose_gray, 25, 255, cv2.THRESH_BINARY_INV)

        nose_area = frame[top_left[1]:top_left[1] + nose_height, top_left[0]:top_left[0] + nose_width]

        nose_area_without_nose = cv2.bitwise_and(nose_area, nose_area, mask=cat_mask)

        nose_output = cv2.add(nose_area_without_nose, cat_nose)

        frame[top_left[1]:top_left[1] + nose_height, top_left[0]:top_left[0] + nose_width] = nose_output

        cv2.imshow('Nose area', cat_nose_gray)
        cv2.imshow('Cat Nose', cat_nose)
        cv2.imshow('Nose Output', nose_output)

    print(nose_top)

    cv2.imshow('Face Filter', frame)




    key = cv2.waitKey(1)

    if key == 27:
        break
