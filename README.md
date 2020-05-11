# Shape Detection
<div>
<p> <b>Current State</b>: Prepares images for shape detection, utilizes basic edge counting for identifying shapes</p>
</div>

<div>
<p><strong>Latest Change</strong>: Crops images to prepare for shape detection </p>
</div>

<div>
<p><strong>Next Goals</strong>: Implement KNN, implement a shape detector to parse through all images return by color detector </p>
</div>
 
How it works:
-------------
<h> Currently uses tools in the OpenCV library, planning to implement KNearestNeighbor (KNN) <h>
 
<b>Step 1: Fill in the hole left by the letter </b>
 <div>
   <p>Reads selected image from color detection and converts to grayscale</p> 
   <p>Threshold the image to change to black and white <p> 
   <p>Floodfills the image and inverts to pull out the letter hole <p>
   <p>Overlay the two images and invert <p>
   <p>Save the new filled in image in filled folder</p>
 </div>
<b>Step 2: Crop the Shape </b>
<div>
   <p>Crops the shape using a bounding recetangle around each contour detected</p>
   <p>Save the cropped shapes in cropped folder </p>
  <p>Note: works for images that may have more than one shape</p>
</div>
<b>Step 3: Shape Detection </b>
 <div>
  <p>Detects the corners and edges of the shapes<p>
  <p>Classifies the shape based on the number of corners and edges<p>
  <p>Note: only works for a very limited amount of shapes,so need to improve that<p>
 </div>


