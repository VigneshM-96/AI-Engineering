from typing import AbstractSet
import numpy as np 

#basic operations
A = np.array([[1, 2] ,[3, 4]])
B = np.array([[5,  6], [7, 8]])

#element-wise
print(A + B)
print(A * B)

#matrix multiplication
print(A @ B) #or np.dot() or np.matmul()

#transpose
print(A.T) 

#determinant
print(np.linalg.det(A))
