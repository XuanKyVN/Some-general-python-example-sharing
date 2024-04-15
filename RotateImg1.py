import cv2
import matplotlib.pyplot as plt
'''
# import required libraries


# load the input image
img = cv2.imread('pic/leaf.jpg')

# cv2.ROTATE_90_CLOCKWISE
# cv2.ROTATE_180
# cv2.ROTATE_90_COUNTERCLOCKWISE

# rotate the image by 180 degree clockwise
img_cw_180 = cv2.rotate(img, cv2.ROTATE_180)

# display the rotated image
cv2.imshow("Image rotated by 180 degree", img_cw_180)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# load the input image
img = cv2.imread('pic/leaf.jpg')

# convert the image to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# rotate the image by 90 degree clockwise
img_cw_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# rotate the image by 270 degree clockwise or 90 degree counterclockwise
img_ccw_90 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# rotate the image by 180 degree clockwise
img_cw_180 = cv2.rotate(img, cv2.ROTATE_180)

# display all the images
plt.subplot(321)   # 2 row, 2 column, index 1
plt.imshow(img, 'gray')
plt.title('Original Image')
plt.axis('on')
# --------------------------

plt.subplot(322), plt.imshow(img_cw_90, 'gray'), plt.title('(90 degree clockwise)'), plt.axis('off')
plt.subplot(323), plt.imshow(img_cw_180, 'gray'),
plt.title('180 degree'), plt.axis('off')

plt.subplot(324), plt.imshow(img_ccw_90, 'gray'),
plt.title('270 degree clockwise/\n 90 degree counter clockwise'), plt.axis('off')


# Convert image to grayscale
plt.subplot(325), plt.imshow(img_ccw_90, 'gray'),
plt.title('Testing Gray Scale'), plt.axis('off')

plt.show()