# Letter Recognition
<div>
<h> Current State: Can recognize numbers and letters but we need to figure out how to make it more accurate<h>
</div>
<div>
<h style= "color:green'"> Latest Change: Now using HOG Features instead of pixel value features for improved accuracy <h>
</div>
 
How it works:
-------------
<h> We will take advantage of a supervised learning technique known as KNearestNeighbor (KNN) <h>
 
<b>Step 1: Collect Data & Train </b>
 <div>
   <p>We make several calls to read training images stored in our TrainingImages folder</p> 
   <p style = "color:green;"> We extract HOG features from these training images <p> 
   <div>![Original Image](TestImage/A.png) ![HogImage](A_HOG.png) </div>
   <p>We organize image features into an array and create a corresponding label array <p>
   <p>Feed these two arrays into the the KNN training class available through openCV <p>
 </div>
<b>Step 2: Reap the reward </b>
 <div>
  <p>Once the training is done we can make calls to find the nearest neighbors for a given test image <p>
 </div>

