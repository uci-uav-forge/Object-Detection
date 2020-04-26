import cv2
import numpy as np
import glob
import os

# number of data points used to train KNN model
NUMBER_OF_DATA_POINTS = 516

# constant image dimensions (test images must match these dimensions)
HEIGHT = 128
WIDTH = 128

# variable used to keep track of data points
number_of_data_points_counter = NUMBER_OF_DATA_POINTS

# creating labels for numbers
nums = np.arange(10)
num_labels = np.repeat(nums, number_of_data_points_counter)

# this is where we will store our number images
num_images = []

# loading images into num_images array
for indx, num in enumerate(nums):
    curr_folder = str(indx)
    path_argument = 'TrainingImages\\' + curr_folder + '\\*.png'
    for filename in glob.glob(path_argument):
        if number_of_data_points_counter > 0:
            curr_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            curr_image = curr_image.flatten()
            num_images.append(curr_image)
            number_of_data_points_counter = number_of_data_points_counter - 1
        else:
            number_of_data_points_counter = NUMBER_OF_DATA_POINTS
            break

# converting our array into numpy array for training
num_images = np.array(num_images, dtype=np.float32)

# creating an instance of the KNN class
knn = cv2.ml.KNearest_create()

# training our model with our images and labels
knn.train(num_images, cv2.ml.ROW_SAMPLE, num_labels)

# reading test image
test_image_arr = []
test_image = cv2.imread('TestImage\\3.png', cv2.IMREAD_GRAYSCALE)
test_image = test_image.flatten()
test_image_arr.append(test_image)
test_image = np.array(test_image_arr, dtype=np.float32)

# testing out our model
ret, result, neighbours, dist = knn.findNearest(test_image, k=1)

print(result)





