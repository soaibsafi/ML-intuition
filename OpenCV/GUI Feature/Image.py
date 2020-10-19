import cv2
import numpy as np

'''
cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
'''

# Load an image in grayscale
img_gray = cv2.imread('test_image.jpg', cv2.IMREAD_GRAYSCALE)

# Display the image
cv2.imshow('Image', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Load an image as color image
img_col = cv2.imread('test_image.jpg', cv2.IMREAD_COLOR)  # instead 1
cv2.imshow('Color Image', img_col)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Load an image with alpha channel
img_alpha = cv2.imread('test_image.jpg', cv2.IMREAD_UNCHANGED)  # instead 1
cv2.namedWindow('Unchanged Image', cv2.WINDOW_NORMAL)
cv2.imshow('Unchanged Image', img_alpha)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Write an image
cv2.imwrite('test_image_grayscaled.jpg', img_gray)

