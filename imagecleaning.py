import cv2 as cv
import numpy as np
import pdb
import argparse
from pathlib import Path, PurePath
import os
#669*497


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True, help="Path to image")
	args = vars(ap.parse_args())
	global remove
	remove = False
	global counter
	counter = 0
	red = []
	orgimg = cv.imread(args['image'])
	img = cv.imread(args['image'], cv.IMREAD_GRAYSCALE)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			if(img[i][j] > 0):
				red.append([i, j])
	print(len(red))
	if(len(red) > 10000):
		for i in red:
			img[i[0]][i[1]] = 0;
			remove = True
	kernel = np.ones((3,5),np.uint8)
	img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
	for i in range(img.shape[0]):
		find = False
		for j in range(img.shape[1]):
			if(img[i][j] > 0):
				counter = counter + 1
				print(counter)
				if(img[i][j] > 0 and counter > 100):
					save_name_org = PurePath("object", Path(args['image']).stem + f"_shape.jpg")
					print(save_name_org)
					cv.imwrite(str(save_name_org), img)
					save_name_org = PurePath("original_good", Path(args['image']).stem + f"_shape.jpg")
					print(save_name_org)
					cv.imwrite(str(save_name_org), orgimg)
					find = True
					break
		if(find == True):
			break
	print(find, counter)
	if(find == False):
		print("here")
		save_name_org = PurePath("trash", Path(args['image']).stem + f".jpg")
		cv.imwrite(str(save_name_org), orgimg)

	cv.waitKey(0)
	cv.destroyAllWindows()

if __name__ == '__main__':
    main()
