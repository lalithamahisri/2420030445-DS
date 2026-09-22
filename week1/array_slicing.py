import numpy as np
p = np.array([1,2,33,45,67,78])
print(p[0])
print(p[5])

q = np.array([[1,2,3],[6,7,8]])
print(q[0,0])

s = np.array([[[1,2,3],[4,5,6],[6,7,8],[9,7,8]]])
print(s[0,1,2])


print(p[2:5])
print(p[-1])
print(p[4:])
print(p[:5])

#Array([start:end:step])