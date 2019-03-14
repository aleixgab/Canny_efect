import cv2
import numpy as np


def convolve(dest, src, i, j, kernel):
    krows, kcols = kernel.shape
    srctmp = src[i:i + krows, j:j + kcols]
    dest[i, j] = (srctmp * kernel[:, :, np.newaxis]).sum(axis=(0, 1))


def execute(img):
    # Load an image
    rows, cols = img.shape

    # Kernel size / radius
    ksize = 5
    kradi = ksize / 2

    # Create the kernel manually
    kernel = np.array([
        [1.,  4.,  7.,  4., 1.],
        [4., 16., 26., 16., 4.],
        [7., 26., 41., 26., 7.],
        [4., 16., 26., 16., 4.],
        [1.,  4.,  7.,  4., 1.]
    ])

    # Create a copy with black padding
    intKradi = int(kradi)
    imgpadding = np.zeros((int(rows) + 2 * intKradi, int(cols) + 2 * intKradi, 1))
    imgpadding[intKradi:-intKradi, intKradi:-intKradi, 0] = img

    # Convolution
    filtered = np.zeros(img.shape)
    for i in range(0, rows):
        for j in range(0, cols):
            convolve(filtered, imgpadding, i, j, kernel)
    filtered /= kernel.sum()

    return (np.uint8(filtered))
