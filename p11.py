# Dot product 
import numpy as np
import array 

# 8 bytes size int 
a = array.array('q') 
for i in range(100000): 
	a.append(i); 

b = array.array('q') 
for i in range(100000, 200000): 
	b.append(i) 

n_dot_product = np.dot(a, b) 
print("\n dot product: ", n_dot_product)

transpose = np.array([[1, 2, 3, 4, 5, 6]]).T
print("\n transpose: \n", transpose)

add = np.add(a,b)
print("\n add: ", add)

subtract = np.subtract(a,b)
print("\n subtract: ", subtract)