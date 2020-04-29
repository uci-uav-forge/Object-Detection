import cv2
import numpy as np

# constant image dimensions (test images must match these dimensions)
HEIGHT = 128
WIDTH = 128

# Loading training data
with np.load('knn_data.npz') as data:
    print(data.files)
    training_data = data['training_images']
    training_labels = data['training_labels']

# creating an instance of the KNN class
knn = cv2.ml.KNearest_create()

# training our model with our images and labels
knn.train(training_data, cv2.ml.ROW_SAMPLE, training_labels)

# reading test image
test_image_arr = []
test_image = cv2.imread('TestImage\\2.png', cv2.IMREAD_GRAYSCALE)
if test_image.shape[0] != 128 or test_image.shape[1] != 128:
    test_image = cv2.resize(test_image, (WIDTH, HEIGHT))
test_image = test_image.flatten()
test_image_arr.append(test_image)
test_image = np.array(test_image_arr, dtype=np.float32)

# testing out our model
ret, result, neighbours, dist = knn.findNearest(test_image, k=3)

# if the result is not an integer give us the ascii character

if result > 10:
    result = chr(int(result[0][0]))

# printing result
print(result)