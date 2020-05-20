""" Run using 'python3 fill_in.py --image *name_of_test_img*'"""

import cv2
import numpy as np 
import argparse
from pathlib import Path

# Read image through script line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

# Read image in grayscale
img = cv2.imread(args['image'], cv2.IMREAD_GRAYSCALE) # for comparing intensities

# Thresholding, cleans the image
# 150 = threshold for pixel value, 150 chosen after testing
# below 150 threshold becomes white, above becomes black
retval, thresh_im = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

# Create a copy of threshold image
floodfill_im = thresh_im.copy()

# Initializing mask for flood filling
height, width = thresh_im.shape[:2]
mask = np.zeros((height + 2, width + 2), np.uint8)

# Floodfill starting from (0,0) with black
cv2.floodFill(floodfill_im, mask, (0,0), 255)
floodfill_im_inv = cv2.bitwise_not(floodfill_im) # invert image

# Overlay images to get filled in 
filled_in_img = thresh_im | floodfill_im_inv

# Invert the final image to make easier for future portions
filled_in_img_inv = cv2.bitwise_not(filled_in_img)

# Save in 'filled' folder
save_name = Path("filled") / Path(args['image']).name
cv2.imwrite(str(save_name), filled_in_img_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
