import cv2 as cv
import numpy as np
import pdb
#669*497

def main():
	img = cv.imread('test.jpg')
	kernel = np.ones((5,5),np.uint8)
	img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

	# for i in range(len(img) - 2):
	# 	for j in range(len(img[1]) - 2):
	# 		if((img[i][j][1] != img[i+1][j][1] or img[i][j][1] != img[i][j+1][1]) and img[i][j][1] > 0):
	# 			img[i][j][1] = 0;
	# 			img[i][j][0] = 0;
	# 			img[i][j][2] = 0;
#turns out this was useless lol
	# 			print(img[i][j])
	# 		if(img[i][j][0] != 0 or img[i][j][1] != 0 or img[i][j][2] != 0):
	# 			equalColorR = img[i][j][0]
	# 			equalColorG = img[i][j][1]
	# 			equalColorB = img[i][j][2]
	# 			tempBlobSize = 0
	# 			tempBlobSize = checkBlobs(img, i, j, equalColorR, equalColorG, equalColorB, 0)
	# 			if(tempBlobSize > maxBlobSize):
	# 				maxi = i
	# 				maxj = j
	# 				maxBlobSize = tempBlobSize
	# print(maxi, maxj)
	# for i in range(15):
	# 	img[i+maxi][maxj][0] = 255
	cv.imshow('image',img)
	cv.waitKey(0)
	cv.destroyAllWindows()

# def checkBlobs(img, i, j, equalColorR, equalColorG, equalColorB, tempBlobSize):
# 	if(i<0 or j<0 or i>len((img) - 1) or j>len((img[1]) - 1)):
# 		print('here')
# 		return tempBlobSize
# 	elif((img[i][j][0] - int(equalColorR) < 10) and (img[i][j][1] - int(equalColorG) < 10) and (img[i][j][2] - int(equalColorB) < 10)):
# 		tempBlobSize+=1
# 		img[i][j][2] = img[i][j][1] = img[i][j][0] = 0
# 		if(j+1 < len(img[1]) -1 ):
# 			return checkBlobs(img, i, j+1, equalColorR, equalColorG, equalColorB, tempBlobSize)
# 	return tempBlobSize

if __name__ == '__main__':
    main()
