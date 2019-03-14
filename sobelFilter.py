import cv2
import numpy as np

def execute(image):

    gx = np.array([[-1,0,1],
                    [-2,0,2],
                    [-1,0,1]])

    gy = np.transpose(gx)

    sobleMat = image
    for i in range(2,image.shape[0]-1):
        for j in range(2, image.shape[1]-1):

            matGX = image[i-1:i+2, j-1:j+2] * gx
            sumGX = matGX.sum()
            matGY = image[i-1:i+2, j-1:j+2] * gy
            sumGY = matGY.sum()

            finalG = np.sqrt(sumGX * sumGX + sumGY * sumGY)

            sobleMat[i-1][j-1] = finalG


    cv2.imshow("Sobel",np.uint8(sobleMat))

    return np.uint8(sobleMat)
