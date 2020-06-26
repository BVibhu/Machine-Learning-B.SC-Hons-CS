import array as arr
a = arr.array('i', [1, 2, 3]) 
  
print ("The new created array is : ", end =" ") 
for i in range (0, 3): 
    print (a[i], end =" ")

rows, cols = (5, 5) 
arr = [[0]*cols]*rows 
print(arr)

ar=[0]*5
print(ar)

ar=[1]*6
print(ar)

import random

# Generate 'n' unique random numbers within a range
randomList = random.sample(range(0, 1000), 10)
print("Printing array of 10 random numbers:",randomList)

import numpy as np
ar= np.matrix('[6, 2; 3, 4]') 
         
# applying matrix.diagonal() method 
m = ar.diagonal() 
   
print(m)