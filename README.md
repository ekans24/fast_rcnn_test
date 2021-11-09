# faster_rcnn_test
Testing out Faster RCCN on Blood cell type data.

# Fast RCNN Algorithm
The follow github implementation of fast rcnn was used: https://github.com/kbardool/keras-frcnn.git  

# Data
The data used was from the BCCD dataset. The full dataset can be downloaded from https://github.com/Shenggan/BCCD_Dataset

# Implementation
The code used to produce the results can be found in the scripts folder.

# Sample image
The images conist of different types of blood cells. The goal is to identify whether the blood cell is a red blood cell, white blood cell or a platelet. Below you can see an example of an image.  
![alt text](https://github.com/ekans24/fast_rcnn_test/blob/master/Dataset/All_images/BloodImage_00005.jpg)

# Another Example
Here are a few sample results produced by the fast rcnn model.
![alt text](https://github.com/ekans24/fast_rcnn_test/blob/master/Results/BloodImage_00005_PREDICT.jpg)
![alt text](https://github.com/ekans24/fast_rcnn_test/blob/master/Results/BloodImage_00051_PREDICT.jpg)
![alt text](https://github.com/ekans24/fast_rcnn_test/blob/master/Results/BloodImage_00054_PREDICT.jpg)
![alt text](https://github.com/ekans24/fast_rcnn_test/blob/master/Results/BloodImage_00089_PREDICT.jpg)

# References
https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/
