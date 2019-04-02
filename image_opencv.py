import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

path = r'H:\DATA\puppy.jpg'


def practise_1():
    # reading image through opencv and using cvtColor,gray,resize and flip functions

    global path
    if os.path.exists(path):
        image = cv2.imread(path)
    else:
        image = None
    image_new = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.subplot(2, 2, 1)
    plt.imshow(image_new)
    image_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    plt.subplot(2, 2, 2)
    plt.imshow(image_gray)
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.resize(image, (250, 250)))
    plt.subplot(2, 2, 4)
    plt.imshow(cv2.flip(image, -1))
    plt.show()
    while True:
        cv2.imshow('puppy', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


def practise_2():
    # Creating rectangle,circle,square,line and polygon shapes on a blank image

    blnk_image = np.zeros((512, 512, 3), np.int16)
    cv2.rectangle(blnk_image, pt1=(200, 100), pt2=(500, 200), color=(200, 150, 200), thickness=20)
    cv2.rectangle(blnk_image, pt1=(100, 100), pt2=(50, 50), color=(0, 0, 255), thickness=5)
    cv2.circle(blnk_image, center=(400, 400), radius=100, color=(0, 255, 0), thickness=-1)
    cv2.line(blnk_image, pt1=(0, 512), pt2=(512, 0), color=(200, 200, 0), thickness=3)
    cv2.putText(blnk_image, text='Blank', org=(20, 512), fontFace=cv2.FONT_ITALIC, fontScale=3, color=(255, 255, 255),
                thickness=2, lineType=cv2.LINE_AA)
    cv2.polylines(blnk_image, pts=[np.array([[200, 500], [100, 100], [400, 300], [300, 250]],
                                            dtype=np.int32).reshape(-1, 1, 2)], color=(0, 200, 200), thickness=3,
                  isClosed=True)
    cv2.fillPoly(blnk_image, pts=[np.array([[10, 300], [75, 200], [150, 300]],
                                           dtype=np.int32).reshape(-1, 1, 2)], color=(0, 200, 200))
    plt.imshow(blnk_image)
    plt.show()


def practise_3():
    # Draw circle with help of mouse
    initial_y, initial_x = -1, -1

    def draw_shape(event, x, y, flags, param):
        global initial_x, initial_y
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img, center=(x, y), radius=20, color=(255, 0, 0), thickness=-1)
        elif event == cv2.EVENT_RBUTTONDOWN:
            initial_x, initial_y = x, y
        elif event == cv2.EVENT_RBUTTONUP:
            cv2.rectangle(img, pt1=(initial_x, initial_y), pt2=(x, y), color=(0, 255, 0), thickness=-1)

    img = np.zeros((512, 512, 3), dtype=np.uint8)
    cv2.namedWindow('drawing')
    cv2.setMouseCallback('drawing', draw_shape)
    while True:
        cv2.imshow('drawing', img)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    practise_3()
