# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:49:03 2021

@author: Ekran
"""

# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches

# read the csv file using read_csv function of pandas
train = pd.read_csv('C:/Users/Ekran/Desktop/blood_cell_detection/Dataset/train.csv')
print(train.head(5))

# reading single image using imread function of matplotlib
image = plt.imread('C:/Users/Ekran/Desktop/blood_cell_detection/Dataset/Train_images/BloodImage_00000.jpg')
plt.imshow(image)

# Number of unique training images
print(train['filename'].nunique())

# Number of classes
print(train['cell_type'].value_counts())

fig = plt.figure()

#add axes to the image
ax = fig.add_axes([0,0,1,1])

# read and plot the image
image = plt.imread('C:/Users/Ekran/Desktop/blood_cell_detection/Dataset/Train_images/BloodImage_00000.jpg')
plt.imshow(image)

# iterating over the image for different objects
for _,row in train[train.filename == "BloodImage_00000.jpg"].iterrows():
    xmin = row.xmin
    xmax = row.xmax
    ymin = row.ymin
    ymax = row.ymax
    
    width = xmax - xmin
    height = ymax - ymin
    
    # assign different color to different classes of objects
    if row.cell_type == 'RBC':
        edgecolor = 'r'
        ax.annotate('RBC', xy=(xmax-40,ymin+20))
    elif row.cell_type == 'WBC':
        edgecolor = 'b'
        ax.annotate('WBC', xy=(xmax-40,ymin+20))
    elif row.cell_type == 'Platelets':
        edgecolor = 'g'
        ax.annotate('Platelets', xy=(xmax-40,ymin+20))
        
    # add bounding boxes to the image
    rect = patches.Rectangle((xmin,ymin), width, height, edgecolor = edgecolor, facecolor = 'none')
    
    ax.add_patch(rect)

data = pd.DataFrame()
data['format'] = train['filename']

# as the images are in train_images folder, add train_images before the image name
for i in range(data.shape[0]):
    data['format'][i] = 'train_images/' + data['format'][i]

# add xmin, ymin, xmax, ymax and class as per the format required
for i in range(data.shape[0]):
    data['format'][i] = data['format'][i] + ',' + str(train['xmin'][i]) + ',' + str(train['ymin'][i]) + ',' + str(train['xmax'][i]) + ',' + str(train['ymax'][i]) + ',' + train['cell_type'][i]

data.to_csv('annotate.txt', header=None, index=None, sep=' ')