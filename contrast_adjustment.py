import cv2
import matplotlib.pyplot as plt


def contrast_adjust(img):
    # applies histogram equalisation for increasing contrast
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
    return cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)


def plot_hist(img):
    for index, color in enumerate(['r', 'g', 'b']):
        hist_value = cv2.calcHist([img], [index], None, [256], [0, 256])
        plt.plot(hist_value)
    plt.show()


if __name__ == '__main__':
    gorilla = cv2.imread(r'H:\DATA\gorilla.jpg')
    plt.imshow(gorilla)
    plt.show()
    contrast_gorilla = contrast_adjust(gorilla)
    plt.imshow(contrast_gorilla)
    plt.show()




