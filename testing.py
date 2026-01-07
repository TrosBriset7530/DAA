
import numpy as np
d = 1; x = 1
for i in range(1,10000):
    x *= i
    d += 1/x
print(d)
arr = np.array([0,1])
pi = 3
for i in range(1,100000):
    pi += 4 * (-1)**(i+1) / (2*i * (2*i+1) * (2*i+2))
print(pi)
print(arr)