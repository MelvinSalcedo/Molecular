# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:12:05 2019

@author: melvin
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2
import time
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

from sklearn.cluster import DBSCAN
import kmedoids
from sklearn.metrics.pairwise import pairwise_distances

import numpy as np
import cv2
img = cv2.imread("entrada2.jpg",1)
height, width, channels = img.shape

print(img.shape)
image = img.reshape(-1, img.shape[-1])

#data = np.arange(60).reshape(20,3)

int_T=int((height*width)/3.0)
print(height,width,int_T)

data = np.arange(height*width-1).reshape(int_T,3)

   
# distance matrix
D = pairwise_distances(data, metric='euclidean')

# split into 2 clusters
M, C = kmedoids.kMedoids(D, 5)

print("______________________")
print('medoids:')

for point_idx in M:
    print( data[point_idx] )

print('')
print('clustering result:')
num=0
for label in C:
    for point_idx in C[label]:
        print('label {0}:　{1}'.format(label, data[point_idx]))
        num+=1
print(num)

kmeansImage = np.zeros(img.shape[:2], dtype=np.uint8)
