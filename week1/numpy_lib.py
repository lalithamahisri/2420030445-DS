import numpy as np
n = np.array([2,3,5,67])
print(type(n))


n = np.array(23)
print(n.ndim)
n = np.array([23])

print(n.ndim)




n = np.array([1,2,3,4,5,6])
print(n)
p = np.array([[1, 2, 4],
              [4, 5, 6]])
print(p)
print(n.ndim)



p = np.zeros([1])
n = np.zeros([3,4])
print(n)
print(type(n))


p = np.ones([1])
n = np.ones([3,4])
print(n)
print(type(n))
