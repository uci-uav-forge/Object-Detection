import cv2
import numpy as np
from HOG_feature_extraction import hog_extractor

# constant image dimensions (test images must match these dimensions)
HEIGHT = 128
WIDTH = 128

# loading number training data
with np.load('knn_number_data.npz') as data:
    number_training_data = data['number_training_images']
    number_training_labels = data['number_training_labels']

# loading alphabet training data
with np.load('knn_alphabet_data.npz') as data:
    alphabet_training_data = data['alphabet_training_images']
    alphabet_training_labels = data['alphabet_training_labels']

# reading test image
test_image_arr = []
test_image = cv2.imread('TestImage\\H.png', cv2.IMREAD_GRAYSCALE)

# extracting hog features and flattening
test_image = hog_extractor(test_image)

test_image_arr.append(test_image)
test_image = np.array(test_image_arr, dtype=np.float32)

# creating an instance of the KNN class
knn = cv2.ml.KNearest_create()

########################################
# Training and Testing Numbers
#########################################
# training our model with our number images
knn.train(number_training_data, cv2.ml.ROW_SAMPLE, number_training_labels)

# testing out our model for numbers
ret_num, result_num, neighbours_num, dist_num = knn.findNearest(test_image, k=3)

#########################################
# Training and Testing Alphabet
#########################################
# training our model with alphabet images
knn.train(alphabet_training_data, cv2.ml.ROW_SAMPLE, alphabet_training_labels)

# testing out our model for alphabet
ret_alpha, result_alpha, neighbours_alpha, dist_alpha = knn.findNearest(test_image, k=3)

##########################################
# Taking Best Estimation Based on Distance
##########################################

average_num_distance = np.mean(dist_num/np.sum(dist_alpha))
average_alpha_distance = np.mean(dist_alpha/np.sum(dist_alpha))

if average_alpha_distance < average_num_distance:
    result = int(ret_alpha)

if average_num_distance < average_alpha_distance:
    result = int(ret_num)

# if the result is not an integer give us the ascii character
if result > 10:
    result = chr(result)

print("Potential Letter:", chr(int(ret_alpha)))
print("Potential Number:", int(ret_num))
print("Average distance for num:", average_num_distance)
print("Average distance for alpha:", average_alpha_distance)
# printing result
print("The computer thinks this is", result)