import cv2
import numpy as np
import gaussianFilter as gausian
import sobelFilter as sobel
import cannyFilter as canny

if __name__ == '__main__':
    image = cv2.imread("sonic.jpg", cv2.IMREAD_GRAYSCALE)

    cv2.imshow("Original", image)

    gauseianImage = gausian.execute(image)
    cv2.imshow("Gausian", gauseianImage)

    GX = np.zeros((image.shape[0], image.shape[1]))
    GY = np.zeros((image.shape[0], image.shape[1]))
    sobelImage, GX, GY = sobel.execute(gauseianImage)
    cv2.imshow("Sobel", sobelImage)

    canny.execute(sobelImage, GX, GY)
    img = sobelImage

    cv2.waitKey()
