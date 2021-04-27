import cv2
from color_detect import detect_color
import argparse
from fill_in import fill_in
from shape_detect import detectShape
from letter_recog import letter_recog
from crop_shape import crop_shape
import numpy as np

'''
    how to run:
        python .\main.py -i ../test_im/testim3.png
        python .\main.py -i ../test_im/testim5.png
        and so on....

    Not implemented with the HSV colors, so it should be kept in mind.
'''

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to image")
    args = vars(ap.parse_args())

    img_path = args['image']
    img = cv2.imread(img_path)

    #detected color image. if returns None (not found) then process is over.

    pack = detect_color(img) #this takes awhile to run
    if type(pack) == type(None):
        print('No interesting color detected.')
        return 0

    color_img, orig_img = pack

    #NOTE: try to find a way to take out the gray spots in an image. I see it a lot, and if we do that, then most of the problems disappear.
    shape_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    shape_img = fill_in(shape_img)


    cv2.imwrite('../filled_shape/shape.jpg', shape_img) #this is to get rid of error in shape_detect could be done better. will update when i have time.
    coord, bound, shape, detected_shape = detectShape('../filled_shape/shape.jpg')

    x_bound, y_bound, w, h = bound
    crop_color = orig_img[y_bound-5: y_bound+h+5, x_bound-5:x_bound+w+5]
    crop_gray = cv2.cvtColor(crop_color,cv2.COLOR_BGR2GRAY)


    crop = crop_shape(crop_gray)
    cv2.imwrite('filled_shape/test.jpg', crop)

    character = letter_recog(crop,7,7)

    print(f'x,y coord: {coord}')
    print(f'shape: {shape}')
    print(f'character: {character}')

    cv2.imshow('color_detection', color_img)
    cv2.imshow('shape', shape_img)
    cv2.imshow('detected_shape', detected_shape)
    cv2.imshow('crop_color', crop_color)
    cv2.imshow('crop gray', crop_gray)
    cv2.imshow('crop', crop)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
