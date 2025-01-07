import numpy as np

a = np.zeros(10) # function inside numpy creates an array with n number of zeroes inside it.
print(a)

b = np.full((2,10),0.7)# function creates a two-dimensional matrix of dimensions 2 x 10 consisting only of the values 0.7.
print(b)

c = np.linspace(0,25,7)#  function divides the values between 0 and 25 in 7 equal parts. The resultant matrix is in the output.
print(c)

print(type(c))# numpy deals exclusively with ndarray, which is a substitute for lists and is far more efficient. 