import cv2


def image_blending(set_watermarking=True):
    # perform blending of images
    path_1 = r'C:\Users\Harikrishnan VK\PycharmProjects\Image Processing\dog_backpack.jpg'
    path_2 = r'C:\Users\Harikrishnan VK\PycharmProjects\Image Processing\watermark_no_copy.png'
    img_1 = cv2.imread(path_1)
    img_2 = cv2.imread(path_2)
    if set_watermarking:
        blend_img = watermarking(img_1, img_2)
        blend_img = cv2.resize(blend_img, (512, 512))
    else:
        blend_img = blending(img_1, img_2)
    while True:
        cv2.imshow('Blended Image', blend_img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


def blending(img1, img2):
    # blending image after resizing them to same shape
    img1 = cv2.resize(img1, (512, 512))
    img2 = cv2.resize(img2, (512, 512))
    blended_img = cv2.addWeighted(img1, 0.4, img2, beta=0.5, gamma=0)
    return blended_img


def watermarking(img1, img2):
    # watermarking first image using second image text
    img2 = cv2.resize(img2, (600, 600))
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.bitwise_not(img2_gray)
    img_region = cv2.bitwise_or(img2, img2, mask=img2_gray)
    x_value = img1.shape[0] - img2.shape[0]
    y_value = img1.shape[1] - img2.shape[1]
    img1_portion = img1[x_value:img1.shape[0], y_value:img1.shape[1]]
    final_image = cv2.bitwise_or(img1_portion, img_region)
    img1[x_value:img1.shape[0], y_value:img1.shape[1]] = final_image
    return img1


if __name__ == '__main__':
    image_blending(set_watermarking=True)
