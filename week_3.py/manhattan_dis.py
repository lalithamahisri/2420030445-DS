import numpy as np
from scipy.spatial import distance

pointA = np.array([2,4,6])
pointB = np.array([5,1,9])

# distance
manhattan_dis = distance.cityblock(pointA,pointB)
print("Euclidean distance:",manhattan_dis)

#similarity(inverse of diatance)
similarity_manhattan = 1/(1+manhattan_dis)

print("manhattan similarity:",similarity_manhattan)