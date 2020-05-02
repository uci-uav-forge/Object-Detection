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
   <p>Read from the thousands of training images stored in our TrainingImages folder</p> 
   <p>Extract HOG features from these training images <p> 
   <p>Organize image features into 1d array and create a corresponding 1d label array <p>
   <p>Save the training data in .npz file for easy and faster access later <p>
   <p>Note: Training can take up to 3 minutes depending on the number of training images chosen</p>
 </div>
<b>Step 2: Train KNN "Model" </b>
<div>
   <p>Load the training information stored in .npz file</p>
   <p>Create a KNN object and train it (built in OpenCV class and methods) </p>
</div>
<b>Step 3: Reap the reward </b>
 <div>
  <p>Once the training is done, we can read our test image, extract its HOG features, and find its nearest feature neighbors (built in OpenCV method) <p>
 </div>


 <b> Example Input Image: </b> 
-------------

![](TestImage/A.png) 

-------------
<b> Example Input HOG Features: </b>
-------------


![](A_HOG.png)

-------------
<b> Example Output: </b> 
-------------

![](example_output.png)
