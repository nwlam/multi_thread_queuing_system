from cv2 import cv2
import matplotlib.pyplot as plt
import numpy as np

img_raw = cv2.imread('./image/close-hematoma-on-arm-woman-260nw-1508537564.webp')
# img_raw = cv2.imread('./image/healing-stages.jpg')
# img_raw = cv2.imread('./image/blur-wound-knee-flows-blood-260nw-1361015012.webp')
# img_raw = cv2.imread('./image/injured-hand-with-blood-on-table-in-hospital-TT8127.jpg')

cv2.imshow('img_raw',img_raw)

# https://www.learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/
# converting from BGR to HSV color space
hsv = cv2.cvtColor(img_raw,cv2.COLOR_BGR2HSV)

hsv_blur = cv2.GaussianBlur(hsv, (9, 9), 0)
cv2.imshow('hsv_blur', hsv_blur)

#https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv
#https://i.stack.imgur.com/gyuw4.png 
# Range for lower red
#lower_red = np.array([0,120,70])
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
mask1 = cv2.inRange(hsv_blur, lower_red, upper_red)

# Range for upper range
#lower_red = np.array([100,120,70])
lower_red = np.array([100,120,70])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsv_blur,lower_red,upper_red)

# Generating the final mask to detect red color
mask = mask1+mask2

res = cv2.bitwise_and(img_raw, img_raw, mask = mask)
cv2.imshow('res', res)


# res_bw=cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
# (thresh, blackAndWhiteImage) = cv2.threshold(res_bw, 127, 255, cv2.THRESH_BINARY)
# contours, h = cv2.findContours(blackAndWhiteImage, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# img_clone = img_raw.copy()
# cv2.drawContours(img_clone, contours, -1, (0, 255, 0), 2)
# cv2.imshow('contour', img_clone)


# ######DILATION########
cv2.imshow('mask', mask)

mask_morphed = mask
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3, 3))
mask_morphed = cv2.erode(mask_morphed, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11, 11))
mask_morphed = cv2.dilate(mask_morphed,kernel, iterations=2)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(13, 13))
mask_morphed = cv2.erode(mask_morphed, kernel, iterations=2)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5, 5))
mask_morphed = cv2.dilate(mask_morphed, kernel)
cv2.imshow('mask_morphed', mask_morphed)


contours, h = cv2.findContours(mask_morphed, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

print(h, "\n")
length = len(h[0])

contours_filtered = []

for i in range(length):
    valid = True
    if h[0][i][3] != -1:
        valid = False
    
    if valid:
        contours_filtered.append(contours[i])

img_clone = img_raw.copy()

h, w, c = img_raw.shape

final_mask = np.zeros((h,w), dtype=np.uint8)

cv2.drawContours(final_mask, contours_filtered, -1, (255), thickness=-1)

cv2.imshow('final_mask', final_mask)

cv2.drawContours(img_clone, contours_filtered, -1, (0, 255, 0), 2)
cv2.imshow('mask_contours2', img_clone)

img_clone = img_raw.copy()
cv2.drawContours(img_clone, contours_filtered, -1, (255), thickness=-1)

# for i in contours_filtered:
#     print(i)

print(contours_filtered)
cv2.imshow('final_img', img_clone)

# res = cv2.bitwise_and(img_raw, img_raw, mask = final_mask)

# gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
  
# cv2.imshow('Original image',res)
# cv2.imshow('Gray image', gray)


cv2.waitKey(0)
cv2.destroyAllWindows()