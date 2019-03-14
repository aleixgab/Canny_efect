import cv2
import numpy as np


def execute(image, GX, GY):
    angleMat = np.zeros((image.shape[0], image.shape[1]))

    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):

            angleMat[i - 1, j - 1] = np.arctan2(GX[i - 1, j - 1], GY[i - 1, j - 1]) * 180 / 3.14159
            if (23 >= angleMat[i - 1, j - 1] >= -23) or (158 <= angleMat[i - 1, j - 1] <= 181) or (
                    -180 <= angleMat[i - 1, j - 1] <= -158):
                angleMat[i - 1, j - 1] = 0
            elif (23 <= angleMat[i - 1, j - 1] <= 68) or (-113 >= angleMat[i - 1, j - 1] >= -158):
                angleMat[i - 1, j - 1] = 45
            elif (68 <= angleMat[i - 1, j - 1] <= 113) or (-68 >= angleMat[i - 1, j - 1] >= -113):
                angleMat[i - 1, j - 1] = 90
            elif (113 <= angleMat[i - 1, j - 1] <= 158) or (-23 >= angleMat[i - 1, j - 1] >= -68):
                angleMat[i - 1, j - 1] = 135

    maxNum = 0
    for i in range(2, image.shape[0] - 2):
        for j in range(2, image.shape[1] - 2):
            if angleMat[i][j] == 0:
                if image[i-1][j] > image[i][j] or image[i+1][j] > image[i][j]:
                    image[i][j] = 0
            elif angleMat[i][j] == 45:
                if image[i+1][j+1] > image[i][j] or image[i-1][j-1] > image[i][j]:
                    image[i][j] = 0
            elif angleMat[i][j] == 90:
                if image[i][j+1] > image[i][j] or image[i][j-1] > image[i][j]:
                    image[i][j] = 0
            elif angleMat[i][j] == 135:
                if image[i-1][j+1] > image[i][j] or image[i+1][j-1] > image[i][j]:
                    image[i][j] = 0

            if image[i][j] > maxNum:
                maxNum = image[i][j]


    capMax = 100
    capMin = 200

    for i in range(2, image.shape[0] - 2):
        for j in range(2, image.shape[1] - 2):
            if image[i][j] > capMax:
                image[i][j] = 255
            elif image[i][j] < capMin:
                image[i][j] = 0

    tmp = image
    for i in range(2, image.shape[0] - 2):
        for j in range(2, image.shape[1] - 2):
            if capMax >= image[i][j] >= capMin:
                if (tmp[i-1][j-1] == 255 or tmp[i][j-1] == 255 or tmp[i+1][j-1] == 255) or (tmp[i-1][j] == 255 or tmp[i][j] == 255 or tmp[i+1][j] == 255) or (tmp[i-1][j-1] == 255 or tmp[i][j-1] == 255 or tmp[i+1][j-1] == 255) :
                    image[i][j] = 255
                else:
                    image[i][j] = 0


    cv2.imshow("Canny", image)
