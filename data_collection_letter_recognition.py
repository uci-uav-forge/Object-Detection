import cv2
import numpy as np
import glob
import os

################################################################################
# variables
################################################################################
# number of data points used to train KNN model
NUMBER_OF_DATA_POINTS = 250

# variable used to keep track of data points
number_of_data_points_counter = NUMBER_OF_DATA_POINTS

# creating labels for alphabet
alphabet_complete = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                     'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alphabet_complete_ascii = [ord(x) for x in alphabet_complete]

alphabet_complete_ascii = np.array(alphabet_complete_ascii)
alphabet_complete_labels = np.repeat(alphabet_complete_ascii, NUMBER_OF_DATA_POINTS)

# creating labels for numbers
nums = np.arange(10)
num_labels = np.repeat(nums, NUMBER_OF_DATA_POINTS)

# this is our complete training array, containing numbers and alphabet images
training_images = []

# this is where we will keep all of our labels
training_labels = np.concatenate((num_labels, alphabet_complete_labels), axis=None)
training_labels = np.array(training_labels, dtype=np.float32)

#################################################################################
# loading number images into training_images array
#################################################################################
for indx, num in enumerate(nums):
    curr_folder = str(indx)
    path_argument = 'TrainingImages\\' + curr_folder + '\\*.png'
    for filename in glob.glob(path_argument):
        # ensuring that we do not exceed the set data point amount
        if number_of_data_points_counter > 0:
            # converting to grayscale
            curr_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            # flattening the image to 1 dimension
            curr_image = curr_image.flatten()
            # appending this one dimensional array to the end of another array
            training_images.append(curr_image)
            # reducing the counter
            number_of_data_points_counter = number_of_data_points_counter - 1
        else:
            # resetting data point counter
            number_of_data_points_counter = NUMBER_OF_DATA_POINTS
            break
##############################################################################
# loading alphabet images to lower_case and upper_case arrays
##############################################################################
for indx, letter in enumerate(alphabet_complete):
    curr_folder = letter
    path_argument = 'TrainingImages\\' + curr_folder + '\\*.png'
    for filename in glob.glob(path_argument):
        # ensuring that we do not exceed the set data point amount
        if number_of_data_points_counter > 0:
            # converting to grayscale
            curr_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            # flattening the image to 1 dimension
            curr_image = curr_image.flatten()
            # appending this one dimensional array to the end of another array
            training_images.append(curr_image)
            # reducing the counter
            number_of_data_points_counter = number_of_data_points_counter - 1
        else:
            # resetting data point counter
            number_of_data_points_counter = NUMBER_OF_DATA_POINTS
            break

# converting our array into numpy array for training
training_images = np.array(training_images, dtype=np.float32)

# saving our training data
np.savez('knn_data.npz', training_images=training_images, training_labels=training_labels)




