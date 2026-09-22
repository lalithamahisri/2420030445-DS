import numpy as np
from scipy.spatial import distance

pointA = np.array([2,4,6])
pointB = np.array([5,1,9])
minkowski_dis_p3 = distance.minkowski(pointA,pointB,p=2)
print("Minkowiski distance(p=3):",minkowski_dis_p3)

#similarity(inverse of distance)
similarity_minkowski = 1/(1+minkowski_dis_p3)

#minkowiski with p=1
minkowski_dis_p3 = distance.minkowiski(pointA,pointB,p=1)
print("Minkowiski distance(p=3):",minkowski_dis_p3)

#similarity(inverse of distance)
similarity_minkowiski = 1/(1+minkowski_dis_p3)

