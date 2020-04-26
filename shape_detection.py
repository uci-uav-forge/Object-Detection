### this function will detect the largest shapes and isolate them ###

import cv2
import numpy as np

def shape_detector(gray_image):

    # sharpening image; make edges stand out
    pre_bilateral = cv2.bilateralFilter(gray_image, 7, 140, 140)
    sharpened = cv2.addWeighted(gray_image, 1, gray_image - pre_bilateral, 3, 0)

    # smoothing images (to remove natural,random textures --ex. grass --- and keep only straight edges)
    median = cv2.medianBlur(sharpened, 7)

    # sharpening noise (emphasizing noise features to make median filter more effective at eliminating them)
    pre_bilateral2 = cv2.bilateralFilter(median, 7, 140, 140)
    sharpened2 = cv2.addWeighted(median, 1, median - pre_bilateral2, 3, 0)

    # smooth image again (minimizes background noise)
    median2 = cv2.medianBlur(sharpened2, 7)

    # final sharpening before canny edge detection (makes for better edges)
    pre_bilateral3 = cv2.bilateralFilter(median2, 7, 140, 140)
    sharpened3 = cv2.addWeighted(median2, 1, median2 - pre_bilateral3, 3, 0)

    # canny edge detection
    canny = cv2.Canny(sharpened3, 0, 80, 1)

    contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(gray_image, contours, -1, (255, 255, 0), 1)

    '''
    while 1:
        k = cv2.waitKey(1) & 0xFF

        contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(gray_image, contours, -1, (255, 255, 0), 1)


        cv2.imshow('gray', gray_image)
        cv2.imshow('prebilateral', pre_bilateral)
        cv2.imshow('gray-prebilat', gray_image-pre_bilateral)
        cv2.imshow('sharpened', sharpened)
        cv2.imshow('median', median)
        cv2.imshow('prebilat2', pre_bilateral2)
        cv2.imshow('sharpened2', sharpened2)
        cv2.imshow('median2', median2)
        cv2.imshow('prebilat3', pre_bilateral3)
        cv2.imshow('sharpened3', sharpened3)
        cv2.imshow('canny', canny)

        if k == ord('q'):
            break
        '''


