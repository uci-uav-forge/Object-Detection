# Image Cleaning
<div>
<p> <b>Current State</b>: CAble to remove small markings from an image with a shape. (isolates the shape). Stil having some trouble with identiying larged bodies since they are disconnected pixels.</p>
</div>

<div>
<p><strong>Latest Change</strong>: Using a dictionary to calculate the number of pixels (using highest R or G or B value) </p>
</div>
 
How it works:
-------------
<h> We will take advantage of a supervised learning technique known as KNearestNeighbor (KNN) <h>
 
<b>Step 1: Pass image to morphology library</b>
 <div>
   <p>Filters the uneccessary pixels but is unable to detect larger bodies</p> 
   <p>Kernel can be manipulated to have a threshold for size but can be innaccurate the smaller the threshold <p>

 </div>
<b>Step 2: Pass Pixels into dictionary" </b>
<div>
   <p>Counts the number of highest taken RGB value for each pixel and places into a dictionary</p>
   <p>Filter the values with a number greater than 600 and smaller than 200</p>
</div>
<b>Step 2: Delete Pixels" </b>
<div>
   <p>Iterate through the pixels and store the ones that are beyond the threshold.</p>
</div>

Future:
-------------

<div>
   <p>Refine the range to be more accurate, and hopefully use Keras to make image cleaning more accurate.</p>
</div>

