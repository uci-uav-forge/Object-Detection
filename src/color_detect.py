from dictionary import colors
import cv2
import numpy as np

def write_color_output(img_path: 'str_to_path includes .jpg or .png'):
    cv2.imwrite('color_detect/'+img_path)

def detect_color(image: 'opencv-image'):
    '''
        Takes in an image and then finds the best colormask of the image.
        This is to find whatever strong color there is inside the image.
        
        It chooses the best image by doing a Hough Transform on the a Canny-Edge version of the colormask
        and then counting the number of lines. (with thresholds to keep it from detecting small blobs)
        
        So I set the number of lines to detect a shape to be between 0 and 90.
        
        returns the colormasked image and then returns a blurred image.
        Note:
            output (colormasked image) is for eventual use with letter_recog
            output_noproc (blurred image) will be for shape_detect
    '''
    for color in colors['Modified_RGB']:
        lower,upper = colors['Modified_RGB'][color]

        #create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        #find colors in the bounds and apply mask
        colormask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=colormask)
        
        #medianBlur 
        output_noprocess = cv2.medianBlur(output, 3)

        kernel = np.ones((2,3),np.uint8) #was 2,2
        output_morphed = cv2.morphologyEx(output_noprocess,cv2.MORPH_OPEN,kernel)

        #preping image for hough transform
        output_morphed = cv2.medianBlur(output_morphed, 7)

        #hough transform
        gray = cv2.cvtColor(output_morphed, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 10, minLineLength=10, maxLineGap=10)
        if type(lines)!=type(None) and (0<lines.shape[0]<=80):
            return (output_noprocess, output) #returns processed image and original masked image

    #if no color is detected to be interesting, then return None and keep going
    return None
