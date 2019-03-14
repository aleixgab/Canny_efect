import cv2
import numpy as np
import gaussianFilter as gausian
import sobelFilter as sobel

if __name__ == '__main__':
    image = cv2.imread("descarga (1).jpg",cv2.IMREAD_GRAYSCALE)

    cv2.imshow("Original", image)

    gauseianImage = gausian.execute(image)
    cv2.imshow("Gausian", gauseianImage)

    sobelImage = sobel.execute(gauseianImage)
    cv2.imshow("Sobel", sobelImage)


    cv2.waitKey()