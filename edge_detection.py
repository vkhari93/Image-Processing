import cv2
import matplotlib.pyplot as plt
import numpy as np


def detect_edge(img):
    blurred_img = blur_image(img)
    low_value, high_value = calc_threshold(img)
    edges = cv2.Canny(blurred_img, threshold1=low_value, threshold2=high_value+50)
    return  edges


def blur_image(img):
    return cv2.GaussianBlur(img, (5, 5), 10)


def calc_threshold(img):
    median = np.median(img)
    low = int(max(0, 0.7*median))
    high = int(min(255, 1.3*median))
    return low, high


if __name__ == '__main__':
    image = cv2.imread(r'H:\Lecture Videos\Python for Computer Vision with OpenCV and Deep Learning\Codes and Data\DATA\Nadia_Murad.jpg')
    new_image = detect_edge(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    plt.imshow(new_image, cmap='gray')
    plt.show()
