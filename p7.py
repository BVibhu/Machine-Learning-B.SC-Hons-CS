import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("maximum value of matrix 'x' is: ", np.max(a))
print("minimum value of matrix 'x' is: ", np.min(a))
print("sum of all elements of matrix 'x' is: ", np.sum(a))
print("Absolute value of matrix 'x' is: ", np.absolute(a))
print("negative value of matrix 'x' is: \n", np.negative(a))

del_new = np.delete(a, 1, 0)
print("After deleting a row: ", del_new)