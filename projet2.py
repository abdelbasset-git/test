from tkinter import *
import numpy as np
import cv2


camera = cv2.VideoCapture(0)
while True:
        ret, frame = camera.read()

        filtre = cv2.GaussianBlur(frame, (5, 5), 0)
        hsv = cv2.cvtColor(filtre, cv2.COLOR_BGR2HSV)

        kernal = np.ones((5, 5), "uint8")


        low_red = np.array([136, 87, 111], np.uint8)
        high_red = np.array([180, 255, 243], np.uint8)
        red_mask = cv2.inRange(hsv, low_red, high_red)
        red = cv2.dilate(red_mask, kernal)
        red1 = cv2.bitwise_and(frame, frame, mask=red_mask)

        contours, ret = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > 200:
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.drawContours(frame, contours, -1, [0, 255, 0], 3)
                cv2.putText(frame, "Red Color", (x - 3, y - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))


        low_blue = np.array([94, 80, 2], np.uint8)
        high_blue = np.array([126, 255, 255], np.uint8)
        blue_mask = cv2.inRange(hsv, low_blue, high_blue)
        blue = cv2.erode(blue_mask, kernal)
        blue1 = cv2.bitwise_and(frame, frame, mask=blue_mask)

        contours, ret = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > 200:
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.drawContours(frame, contours, -1, [0, 255, 0], 3)
                cv2.putText(frame, "Blue Color", (x - 3, y - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))


        low_green = np.array([65, 60, 60], np.uint8)
        high_green = np.array([80, 255, 255], np.uint8)
        green_mask = cv2.inRange(hsv, low_green, high_green)
        green = cv2.dilate(green_mask, kernal)
        green1 = cv2.bitwise_and(frame, frame, mask=green_mask)

        contours, ret = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > 200:
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.drawContours(frame, contours, -1, [0, 255, 0], 3)
                cv2.putText(frame, "Green Color", (x - 3, y - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))


        low_yellow = np.array([20, 100, 100], np.uint8)
        high_yellow = np.array([30, 255, 255], np.uint8)
        yellow_mask = cv2.inRange(hsv, low_yellow, high_yellow)
        yellow = cv2.dilate(yellow_mask, kernal)
        yellow1 = cv2.bitwise_and(frame, frame, mask=yellow_mask)

        contours, ret = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > 200:
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.drawContours(frame, contours, -1, [0, 255, 0], 3)
                cv2.putText(frame, "Yellow Color", (x - 3, y - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 210, 210))

        cv2.imshow('Camera', frame)
        cv2.imshow('Red_Mask', red)
        cv2.imshow('Blue_Mask', blue)
        cv2.imshow('Green_Mask', green)
        cv2.imshow('Yellow_Mask', yellow)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()

