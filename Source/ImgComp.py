import cv2
import numpy as np


original = cv2.imread("C:/Users/gkami/Documents/GitHub/ImageComparissonDualCam/test_files/1.jpg")
duplicate = cv2.imread("images/duplicate.jpg")

def testShow():
    cv2.imshow("1", original)
    cv2.waitKey(0)


