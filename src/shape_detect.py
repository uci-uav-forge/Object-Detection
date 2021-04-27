import cv2
import numpy as np

def detectShape(img_path: 'path string to image'):
    """
    Will take an image and use edge detection to find the high frequency changes to detect edges
    Parameters: nothing
    Returns: returns the image that outlines the shapes and tells what shape it is

    """

    img = cv2.imread(img_path)

    #filter out unwanted dots after gray
    gray = cv2.medianBlur(img, 9)
    gray = cv2.medianBlur(img, 9)
    kernel = np.ones((3,5),np.uint8)
    gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    
    contours, hierachy = cv2.findContours(threshold,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #needs to be right after cvtColor method
    font = cv2.FONT_HERSHEY_COMPLEX

    for cnt in contours:
        arc = cv2.arcLength(cnt,True)
        if arc < 30:
            continue

        #low error approxPoly to get correct bounding box
        #high error to detect shape properly
        approx = cv2.approxPolyDP(cnt,0.07*arc,True) #approx is x,y and it wrong janky
        approx_forbound = cv2.approxPolyDP(cnt,0.01*arc,True) #approx is x,y and it wrong

        cv2.drawContours(img, [approx_forbound], -1, (0, 255, 0), 2) #surrounds the shape
        
        approx_reshape = approx_forbound.reshape(-1,2)
        
        x = int(np.mean(approx_reshape[:,0]))
        y = int(np.mean(approx_reshape[:,1]))
        x_bound, y_bound, w, h = cv2.boundingRect(cnt)

        len_approx = len(approx)
        shape_str = ''

        cv2.circle(img, (x,y), 5, (0,255,0), -1)
        
        if len_approx==3:
            shape_str = 'Triangle'
            cv2.putText(img,"Triangle", (x,y),font,0.5,(255,0,0),1)
        elif len_approx==4:
            aspectRatio = float(w)/h
            if aspectRatio >= 0.95 and aspectRatio <=1.05:
                shape_str = 'Square'
                cv2.putText(img, "Square", (x, y), font, 0.5, (255, 0, 0), 1)
            else:
                shape_str = 'Rectangle'
                cv2.putText(img,"Rectangle", (x,y),font,0.5,(255,0,0),1)
        elif len_approx == 5:
            shape_str = 'Pentagon'
            cv2.putText(img, "Pentagon", (x, y), font, 0.5, (255, 0, 0), 1)
        else:
            shape_str = 'Circle'
            cv2.putText(img, "Circle", (x, y), font, 0.5, (255, 0, 0), 1)

    return ((x,y), (x_bound,y_bound,w,h), shape_str, img) #returns x,y bounding box info, shape_string, and the image