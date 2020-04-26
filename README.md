# Letter Recognition

<h> Current State: Can recognize numbers (can be trained to recognize more features like capital and miniscule
 english letters<h>
 
How it works:
-------------
<h> We will take advantage of a supervised learning technique known as KNearestNeighbor (KNN) <h>
 
<b>Step 1: Train the model </b>
 <div>
   <p>We make several calls to read training images stored in our TrainingImages folder</p> 
   <p>We organize these images into an array and create a corresponding label array <p>
   <p>Feed these two arrays into the the KNN training class available through openCV <p>
 </div>
<b>Step 2: Reap the reward </b>
 <div>
  <p>Once the training is done we can make calls to find the nearest neighbors for a given test image <p>
 </div>

