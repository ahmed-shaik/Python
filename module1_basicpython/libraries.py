import numpy as np
import math
# important components Function, Variable
# Python File Module
# Library = Multiple modules
# Package = Collection of multiple libraries


# User defined Library
# Numpy (Numerical Computation with Arrays)
# - Matplotlib ( Data Visualization)
# Pandas (Data Manipulation/ Data Preprocessing)

# Numpy Numerical Python
# Main object - Array

# Difference between List and Array(Numpy)
#1)arrays have Broadcasting
#2) arrays are faster

# a=[2,4,6,8,10]
# print (a)
# print (type(a))
# a/2 # give an error message

# import numpy as np
# a=np.array([2,4,6,8,10])
# print(a)
# print(type(a))
# print(a/2)

#Single Dimension Vector
# Two Dimension - Matrix
# Three or more dimension Tensor

# b=np.array([[2,4,5,6,7],
#             [1,2,3,4,5]])
# print(b.ndim)

#NUmpy methods:
# np.add()
# np.subtract()
# np.where()
# np.dot()
# np.ptp()
# np.sum()
# np.max()
# np.min()
# np.mean()
# np.median()

# x = np.array([3,4])
# y = np.array([7,6])
# # print(x+y)
# print(np.add(x,y))
# # print(x-y)
# print(np.subtract(x,y))

# print(np.sum(x))

# print(np.mean(x))
# print(np.median(x))
# print(np.min(x))
# print(np.max(x))

#Numpy Operations:
# Euclidean Distance
# Normalization using Min Max Scalar
# Matrix Multiplication (Dot Product)
# Mean Squared Error

# # Euclidean Distance
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[7, 8], [9, 10],[11, 12]])
# # print(math.sqrt((a[1]-a[0])*(a[1]-a[0])+(b[1]-b[0])*(b[1]-b[0])))
# print(np.sqrt(np.sum(np.square(np.subtract(a,b)))))

# Normalization using Min Max Scalar
# a = np.array([6,5,78,153,89])
# for i in a:
#     i = (i-np.min(a))/(np.max(a)-np.min(a))
#     print(i)
    
 
# #Matrix Multiplication (Dot Product)
# print(np.dot(a,b))

# Mean Squared Error
y_pred = np. array( [110, 220, 330] )
y_real = np. array( [100, 200, 300] )

error = np.subtract(y_pred, y_real)
sq = np.square(error)
mse = np.mean(sq)

print('Mean Squared Error:', mse)