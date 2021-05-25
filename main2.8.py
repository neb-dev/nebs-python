# OpenCV
# import cv2
# grayscale_img = cv2.imread("/Users/joshua.nebeker/Desktop/nebs-python/files/smallgray.png", 0) - loads image (0 for grayscale, 1 for bgr OpenCV uses blue,green,red instead of rbg)
# grayscale - returns two dimensonal numpy.ndarray

# bgr_img = cv2.imread("/Users/joshua.nebeker/Desktop/nebs-python/files/smallgray.png", 1)
# bgr - returns three dimensional numpy array (first is blue layer, second is green, third is red) bgr

# cv2.imwrite("newsmallgray.png", grayscale_img) - returns True and creates image from numpy array and stores in the current jupyter python notebook directory


# slicing a python list
# list_data = [1,2,3]
# 1 = 0 index, 2 = 1 index, 3 = 2 index

# list_data[0:1] - returns first element in list (1)
# list_data[0:2] - returns first two elements in list (1,2)
# list_data[-1] - returns last element in list (3)
# list_data[:-1] - returns first two elements in list (1,2)

# slicing a numpy array
# grayscale_img.shape - returns (3,5) (3x5 two dimensional numpy array)
# grayscale_img[0:2] - returns first two rows (0:2 being the index for the rows)
# grayscale_img[0:2,2:4] - returns columns 3 and 4 (2:4 being the index for the columns)
# grayscale_img[2,4] - returns last element in array (182)

# iterate through numpy array
# for el in grayscale_img:
#     print(el) - prints elements in rows 3X5

# for el in grayscale_img.T:
#     print(el) - prints element in columns 5X3

# for el in grayscale_img.flat:
#     print(el) - prints each element 1x1


# stacking numpy arrays
# hstacked = numpy.hstack((grayscale_img,grayscale_img)) - pass Tuple of two numpy arrays to stack horizontally (3x10)
# vstacked = numpy.vstack((grayscale_img,grayscale_img)) - stack vertically 6x5

# splitting numpy arrays
# horizontalsplit = numpy.hsplit(hstacked, 5) - hstacked (3x10) will produce five arrays (3x2, 3x2, 3x2, 3x2, 3x2)
# verticalsplit = numpy.vsplit(vstacked, 3) - vstacked (6x5) wll produce three arrays (2x5, 2x5, 2x5)
# splitting a numpy array will produce a regular python List meaning you can verticalsplit[0] to return the first 2x5 list element
