# Letter Recognition
<div>
<p> <b>Current State</b>: Can recognize numbers and letters but we need to figure out how to make it more accurate</p>
</div>

<div>
<p><strong>Latest Change</strong>: Now using HOG Features instead of pixel value features for improved accuracy </p>
</div>
 
How it works:
-------------
<h> We will take advantage of a supervised learning technique known as KNearestNeighbor (KNN) <h>
 
<b>Step 1: Collect Data & Train </b>
 <div>
   <p>We make several calls to read training images stored in our TrainingImages folder</p> 
   <p>We extract HOG features from these training images <p> 
   <p>We organize image features into an array and create a corresponding label array <p>
   <p>Feed these two arrays into the the KNN training class available through openCV <p>
 </div>
<b>Step 2: Reap the reward </b>
 <div>
  <p>Once the training is done we can make calls to find the nearest neighbors for a given test image <p>
 </div>

<div> <b> Example HOG Feature: </b> </div>

![](TestImage/A.png) ![](A_HOG.png)
