import cv2
import numpy as np

if __name__ == '__main__':
    image = cv2.imread("descarga (1).jpg",cv2.IMREAD_GRAYSCALE)

    newImage = np.zeros([image.shape[0]+4,image.shape[1]+4])
    newImage[2:image.shape[0] + 2,2:image.shape[1] + 2] = image





    gx = np.array([[-1,0,1],
                   [-2,0,2],
                   [-1,0,1]])

    gy = np.transpose(gx)

    sobleMat = newImage
    for i in range(2,newImage.shape[0]):
        for j in range(2, newImage.shape[1]):

            currMat = newImage[i-1:i+2, j-1:j+2]

            if currMat.shape[0] == 3 and currMat.shape[1] == 3:

                matGX = currMat * gx
                sumGX = matGX.sum()
                matGY = currMat * gy
                sumGY = matGY.sum()

                finalG = np.sqrt(sumGX * sumGX + sumGY * sumGY)

                sobleMat[i-1][j-1] = finalG


    cv2.imshow("image",np.uint8(sobleMat))
    cv2.waitKey()