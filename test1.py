import cv2
import numpy as np
import argparse

def process_image(input_filename):
    image = cv2.imread(input_filename)
    blank_image = np.zeros_like(image)
    image = cv2.GaussianBlur(image, (7, 7), 0)
    edges = cv2.Canny(image, 30, 70)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 0:
            cv2.drawContours(blank_image, contour, -1, (255, 255, 255), 3)
    drawing = cv2.bitwise_not(blank_image)
    cv2.imshow("Drawing", drawing)
    cv2.imshow('Image with Contours', image)
    cv2.imshow('Blank Image with Contours', blank_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process an image with contours')
    parser.add_argument('input_filename', type=str, help='Input image filename')
    args = parser.parse_args()
    process_image(args.input_filename)
