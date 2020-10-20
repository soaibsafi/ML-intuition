import cv2
import numpy as np

# load the image
img = cv2.imread('../GUI Feature/test_image.jpg')

# Getting a pixel value -> [b,g,r]
px = img[100, 100]
#print(px)

# Access the blue value
px_b = img[100, 100, 0]
#print(px_b)

# Modify the blue pixel
img.itemset((100, 100, 0), 100)
print(img.item(100,100,0))

# Accessing image properties
print('Shape:', img.shape)
print('Total no of pixel: ', img.size)
print('Image data type: ', img.dtype)


crop = img[33:163, 45:155]
img[273:403, 100:210] = crop

b, g, r = cv2.split(img)
print(b)

b = img[:, :, 1]
cv2.imshow('Image', b)
cv2.waitKey(0)
cv2.destroyAllWindows()
