import numpy as np
import cv2
def crop_shape(img):
    retval, thresh_im = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)

    height, width = thresh_im.shape[:2]
    mask = np.zeros((height + 2, width + 2), np.uint8)

    cv2.floodFill(thresh_im, mask, (0,0), 255)
    img =  cv2.bitwise_not(thresh_im) #should get letter

    contours, _ = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = cv2.boundingRect(contours[0])
    return img[y - 10:y + h + 10, x - 10:x + w + 10]