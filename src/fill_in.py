""" Run using 'python3 fill_in.py --image *name_of_test_img*'"""

import cv2
import numpy as np 
import argparse
from pathlib import Path

'''
# Read image through script line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
'''


def fill_in(img: 'opencv-image but grayscaled'):
    # Read image in grayscale

    retval, thresh_im = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)

    # Create a copy of threshold image
    floodfill_im = thresh_im.copy()

    # Initializing mask for flood filling
    height, width = thresh_im.shape[:2]
    mask = np.zeros((height + 2, width + 2), np.uint8)

    # Floodfill starting from (0,0) with black
    cv2.floodFill(floodfill_im, mask, (0,0), 255)
    floodfill_im_inv = cv2.bitwise_not(floodfill_im) # invert image
    #floodfill_im_inv = floodfill_im

    # Overlay images to get filled in 
    filled_in_img = thresh_im | floodfill_im_inv

    #save_name = Path("filled") / Path(args['image']).name
    return filled_in_img