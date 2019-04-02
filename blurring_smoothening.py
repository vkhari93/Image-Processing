import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_img(path):
    # load image from path provided
    load_image = cv2.imread(path).astype(np.float32)/255
    load_image = cv2.cvtColor(load_image, cv2.COLOR_BGR2RGB)
    return load_image


def display_img(img):
    plt.imshow(img)
    plt.show()


def gamma_correction(img, gamma_val):
    # each value in image is multiplied by a constant gamma to improve brightness.
    # if gamma < 1, image is brighter and if gamma > 1 it will be darker
    corrected_img = np.power(img, gamma_val)
    display_img(corrected_img)
    return corrected_img


def blurring(img, blur_type):
    # blur image using custom low pass filter kernel or using default methods - blur, gausian or median

    if blur_type == 'blur':
        blured_img = cv2.blur(img, ksize=(10, 10))
    elif blur_type == 'custom':
        custom_kernel = np.ones((5, 5), dtype=np.float32) / 25
        blured_img = cv2.filter2D(img, ddepth=-1, kernel=custom_kernel)
    elif blur_type == 'gausian':
        blured_img = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=10)
    elif blur_type == 'median':
        blured_img = cv2.medianBlur(img, 5)
    display_img(blured_img)


if __name__ == '__main__':
    path = r'H:\DATA\dog.jpg'
    image = load_img(path)
    display_img(image)
    gamma = 1/6
    bright_image = gamma_correction(image, gamma)
    blurring(image, blur_type='median')
    blurring(bright_image, blur_type='median')




