import cv2
from skimage.feature import hog
from skimage import data, exposure

# constant image dimensions (test images must match these dimensions)
HEIGHT = 128
WIDTH = 128


# this function returns a one dimensional HOG feature vector
def hog_extractor(gray_img):

    if gray_img.shape[0] != 128 or gray_img.shape[1] != 128:
        gray_img = cv2.resize(gray_img, (WIDTH, HEIGHT))

    fd, hog_image = hog(gray_img, orientations=8, pixels_per_cell=(16, 16),
                        cells_per_block=(1, 1), visualize=True, multichannel=False)
    
    return fd

