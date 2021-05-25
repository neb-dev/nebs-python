# OpenCV
# import cv2
# grayscale_img = cv2.imread("/Users/joshua.nebeker/Desktop/nebs-python/files/smallgray.png", 0) - loads image (0 for grayscale, 1 for bgr OpenCV uses blue,green,red instead of rbg)
# grayscale - returns two dimensonal numpy.ndarray

# bgr_img = cv2.imread("/Users/joshua.nebeker/Desktop/nebs-python/files/smallgray.png", 1)
# bgr - returns three dimensional numpy array (first is blue layer, second is green, third is red) bgr

# cv2.imwrite("newsmallgray.png", grayscale_img) - returns True and creates image from numpy array and stores in the current jupyter python notebook directory