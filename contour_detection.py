import cv2
import sys
import numpy as np
sys.path.append(r'C:\Users\Harikrishnan VK\PycharmProjects\Scripts\Object detection')
import matplotlib.pyplot as plt
from edge_detection import detect_edge


def contour(img):
    contours, hierarchy = cv2.findContours(img, mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)
    canvas = np.zeros(img.shape)
    print(len(contours))
    for i in range(len(contours)):
        if hierarchy[0][i][3] == -1:
            cv2.drawContours(canvas, contours, i, 255, thickness=-1)
    plt.imshow(canvas, cmap='gray')
    plt.show()


image = cv2.imread(r'H:\DATA\dog_face.jpg', 0)
new_image = detect_edge(image)
contour(new_image)

