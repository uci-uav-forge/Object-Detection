import numpy as np
import cv2
import argparse
from pathlib import Path, PurePath
import numpy as np
import pdb

# Read image through script line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

# Process Gray Scale image for corner detection
img = cv2.imread(args['image'], cv2.IMREAD_GRAYSCALE)

# Setting a threshold to select the shape
retval, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

# Detect the contour of the shape
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Make bounding rectangle over each contour and crop and save into "cropped" folder
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(img[i][j] > 0):
            for num, contour in enumerate(contours):
                x, y, w, h = cv2.boundingRect(contour)
                crop = img[y - 25:y + h + 25, x - 25:x + w + 25]
                save_name = PurePath("cropped", Path(args['image']).stem + f"_shape{num + 1}.jpg")
                cv2.imwrite(str(save_name), crop)
        else:
            save_name = PurePath("trash", Path(args['trash'].stem + ".jpg"))

cv2.waitKey(0)
cv2.destroyAllWindows()
