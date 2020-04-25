import numpy as np
import cv2


def detectEdges(img):
    #read the shape filled image given
    img = cv2.imread(img)
    print(img)
    #convert from RGB to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detect the edges
    edges = cv2.Canny(gray, threshold1=30, threshold2=100)

    #display the image with edge detection
    cv2.namedWindow('edges',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('edges', 1000,600)
    cv2.imshow("edges", edges)
    cv2.imwrite("edges.jpg", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detectCorners(img,minDist):
    #minDist is thr minimum distance used to find a corner that is next to another corner
    #it will be different based on our cropping
    #the better the cropping we can use proper euclidean distance to find the threshold
    
    img = cv2.imread(img)
    print(img)
    # convert from RGB to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #find the corners of the shape
    gray = np.float32(gray)
    corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, minDist)
    corners = np.int0(corners)

    #draw points at each corner to make it easier to visualize
    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(img,(x,y),3,255,-1)

    #display the corner detected image
    cv2.namedWindow('Corners', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Corners', 1000, 600)
    cv2.imshow('Corners', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
