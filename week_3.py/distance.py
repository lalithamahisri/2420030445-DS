import numpy as np
from scipy.spatial import distance

pointA = np.array([2,4,6])
pointB = np.array([1,3,5])

#Euclidean distance
euclidean_dis = distance.euclidean(pointA,pointB)
print("Euclidean distance:",euclidean_dis)

#similarity(inverse of diatance)
similarity_euclidean = 1/(1+euclidean_dis)

print("Euclidean similarity:",similarity_euclidean)