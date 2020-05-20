import cv2
import numpy as np
import glob
import os
from HOG_feature_extraction import hog_extractor

############################
# Declaring Useful Variables
############################
# number of data points used to train for numbers
NUMBER_OF_DATA_POINTS_NUM = 200

# number of data points used to train for alphabet
NUMBER_OF_DATA_POINTS_ALPHA = 200

# variable used to keep track of number data points
number_data_points_counter = NUMBER_OF_DATA_POINTS_NUM

# variable used to keep track of alphabet data points
alpha_data_points_counter = NUMBER_OF_DATA_POINTS_ALPHA

# creating labels for alphabet
alphabet_label_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alphabet_label_array_ascii = [ord(x) for x in alphabet_label_array]

alphabet_label_array_ascii = np.array(alphabet_label_array_ascii)
alphabet_label_array_ascii = np.repeat(alphabet_label_array_ascii, NUMBER_OF_DATA_POINTS_ALPHA)
alphabet_label_array_ascii = np.array(alphabet_label_array_ascii, dtype=np.float32)

# creating labels for numbers
nums = np.arange(10)
number_training_labels = np.repeat(nums, NUMBER_OF_DATA_POINTS_NUM)
number_training_labels = np.array(number_training_labels, dtype=np.float32)

# this is our number training array
number_training_images = []

# this is our alphabet training array
alphabet_training_images = []

# this is where we will keep all of our labels
# training_labels = np.concatenate((num_labels, alphabet_complete_labels), axis=None)
# training_labels = np.array(training_labels, dtype=np.float32)

#################################################################################
# Loading Number Images
#################################################################################
for indx, num in enumerate(nums):
    curr_folder = str(indx)
    path_argument = 'TrainingImages\\' + curr_folder + '\\*.png'
    for filename in glob.glob(path_argument):
        # ensuring that we do not exceed the set data point amount
        if number_data_points_counter > 0:
            # converting to grayscale
            curr_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            # extracting hog features and flattening
            curr_image = hog_extractor(curr_image)
            # appending this one dimensional array to the end of another array
            number_training_images.append(curr_image)
            # reducing the counter
            number_data_points_counter = number_data_points_counter - 1
        else:
            # resetting data point counter
            number_data_points_counter = NUMBER_OF_DATA_POINTS_NUM
            break
##############################################################################
# Loading Alphabet Images
##############################################################################
for indx, letter in enumerate(alphabet_label_array):
    curr_folder = letter
    path_argument = 'TrainingImages\\' + curr_folder + '\\*.png'
    for filename in glob.glob(path_argument):
        # ensuring that we do not exceed the set data point amount
        if alpha_data_points_counter > 0:
            # converting to grayscale
            curr_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            # extracting hog features and flattening
            curr_image = hog_extractor(curr_image)
            # appending this one dimensional array to the end of another array
            alphabet_training_images.append(curr_image)
            # reducing the counter
            alpha_data_points_counter = alpha_data_points_counter - 1
        else:
            # resetting data point counter
            alpha_data_points_counter = NUMBER_OF_DATA_POINTS_ALPHA
            break

###########################
# Saving Images and Labels
###########################

# converting our image training images array into numpy array
alphabet_training_images = np.array(alphabet_training_images, dtype=np.float32)

# converting our number training images array into numpy array
number_training_images = np.array(number_training_images, dtype=np.float32)

# saving our number training data
np.savez('knn_number_data.npz', number_training_images=number_training_images,
         number_training_labels=number_training_labels)

# saving our alphabet training data
np.savez('knn_alphabet_data.npz', alphabet_training_images=alphabet_training_images,
         alphabet_training_labels=alphabet_label_array_ascii)




