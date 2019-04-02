import cv2
import matplotlib.pyplot as plt
import numpy as np


def display_img(img):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


def detect_corner(img, method):
    gray_img = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    if 'harris' in method.lower():
        # harris corner detection method
        corner_value = cv2.cornerHarris(gray_img, blockSize=2, ksize=3, k=0.1)
        img[corner_value > 0.01*img.max()] = (255, 0, 0)
    elif 'features' in method.lower():
        # good featues to track corner detection method
        corner_value = np.int0(cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 2))
        for i in corner_value:
            x, y = i.ravel()
            img = cv2.circle(img, (x, y), 2, (255, 0, 0), -1)

    display_img(img)


if __name__ == '__main__':
    actual_img = cv2.imread(r'H:\DATA\real_chessboard.jpg')
    display_img(actual_img)
    detect_corner(actual_img, 'features')


