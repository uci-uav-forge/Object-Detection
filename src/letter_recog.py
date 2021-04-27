import numpy as np
import cv2
from HOG_feature_extraction import hog_extractor

def letter_recog(img, k_num=5,k_alph=5):
    '''
        Letter recognition takes in an image and 2 k-values for knn.
        Trains 2 knn and then detects image.
        
        Returns: character of what should be detected
        
        Note: If we want to take multiple pictures, it'd be better to leave it out to only train it once.
    '''
    img = np.array([hog_extractor(img)], dtype=np.float32)
    
    #get data
    with np.load('knn_number_data.npz') as data:
        number_training_data=data['number_training_images']
        number_training_labels=data['number_training_labels']

    with np.load('knn_alphabet_data.npz') as data:
        alphabet_training_data=data['alphabet_training_images']
        alphabet_training_labels=data['alphabet_training_labels']

    #init knn
    knn = cv2.ml.KNearest_create()

    #knn model for number
    knn.train(number_training_data, cv2.ml.ROW_SAMPLE, number_training_labels)
    ret_num, result_num, neighbors_num, dist_num = knn.findNearest(img, k=k_num)

    #knn model for alphabet
    knn.train(alphabet_training_data,cv2.ml.ROW_SAMPLE, alphabet_training_labels)
    ret_alph, result_alph, neighbors_alph, dist_alph = knn.findNearest(img, k=k_alph)

    #calc distance and then compare between num knn and alphabet knn
    avg_num_dist = np.mean( dist_num/np.sum(dist_num) )

    avg_alph_dist = np.mean( dist_alph/np.sum(dist_alph) )

    if avg_num_dist < avg_alph_dist:
        result = int(ret_num)
    else:
        result = int(ret_alph)

    if result > 10:
        result = chr(result)

    return result
