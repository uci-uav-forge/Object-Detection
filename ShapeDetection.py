import numpy as np
import cv2

#Here are some sample images that came from google and the object detection github
#to test the code itself if you are lazy

#img = cv2.imread("/Users/niva.ranavat/UAVGroundStation/Object-Detection/objy.png")
#img = cv2.imread("/Users/niva.ranavat/Downloads/test2.jpg")
img  = cv2.imread("/Users/niva.ranavat/Downloads/allshapes.jpg")

class Object:
    """
    Will think of a better name
    The shape object
    -able to find the sides and the vertices of the object that it found in the image
    -using those it will classify the type of polygon
    """

    def __init__(self, img):
        #should be the
        self.img = img

    def detectEdges(self):
        """
        Will take an image and use edge detection to find the high frequency changes to detect edges
        Parameters: Nothing
        Returns: numpy array of an image with only the edges

        """

        # read the shape filled image given
        img = cv2.imread(self.img)
        # convert from RGB to gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detect the edges
        edges = cv2.Canny(gray, threshold1=30, threshold2=100)

        # display the image with edge detection
        # comment out if it is too much
        cv2.namedWindow('edges', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('edges', 1000, 600)
        cv2.imshow("edges", edges)
        cv2.imwrite("edges.jpg", edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return edges

    def detectCorners(self, minDist):
        """
         Will take an image and use edge detection to find the high frequency changes to detect edges
         Parameters: minDist -> int
                    - depending on the size of the object in your image, it will find corners that are at least this distance
         Returns: numpy array of coordinate points where the vertices are

        """
        img = cv2.imread(self.img)
        # convert from RGB to gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # find the corners of the shape
        gray = np.float32(gray)
        corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, minDist)
        corners = np.int0(corners)

        # draw points at each corner to make it easier to visualize
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(img, (x, y), 3, 255, -1)

        # display the corner detected image
        cv2.namedWindow('Corners', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Corners', 1000, 600)
        cv2.imshow('Corners', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return corners

    def detectShape(self):

        """
        Will take an image and use edge detection to find the high frequency changes to detect edges
        Parameters: nothing
        Returns: returns the image that outlines the shapes and tells what shape it is

        """
        #copy of the original image so we don't change that
        img = self.img
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

        #contours are a curve simply joins a bunch of continous points that have the same color or intensity
        # in our case it will help find the edges of the shape
        contours, hiearachy = cv2.findContours(threshold,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        font = cv2.FONT_HERSHEY_COMPLEX
        # cv2.drawContours(img, contours, -1, (0,255,0), 3)

        #using each of the contours, estimate the different separate edges of a shape
        #it will print and outline the shape name on the image
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            #color = cv2.Scalar(0,255,0)
            if len(approx)==3:
                cv2.putText(img,"Triangle", (x,y),font,0.5,(0,0,0),1)
            elif len(approx)==4:
                x,y,w,h = cv2.boundingRect(approx)
                aspectRatio = float(w)/h
                if aspectRatio >= 0.95 and aspectRatio <=1.05:
                    cv2.putText(img, "Square", (x, y), font, 0.5, (0, 0, 0), 1)
                else:
                    cv2.putText(img,"Rectangle", (x,y),font,0.5,(0,0,0),1)
            elif len(approx) == 5:

                cv2.putText(img, "Pentagon", (x, y), font, 0.5, (0, 0, 0), 1)
            else:
                print(approx)
                cv2.putText(img, "Circle", (x, y), font, 0.5, (0, 0, 0), 1)



            #displays the image and the image where the detected shapes are displayed with the classification name
            cv2.imshow("img",img)
            cv2.imwrite("shapesdetected.jpg",img)
            #cv2.imshow("threshold", threshold)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return img
