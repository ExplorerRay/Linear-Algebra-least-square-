import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

x=np.array([15,14,13,12,11,10,8,7])
b=np.array([29,20,55,107,92,73,110,18])

# assemble matrix A
A = np.vstack([x, np.ones(len(x))]).T


# turn b into a column vector
b = b[:, np.newaxis]


#\hat{x}= (A^TA)^{-1} A^T b
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),b)
print(alpha)#[[斜率][y截距]]


plt.figure(figsize = (10,8))
plt.plot(x, b, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('days before final exam week')
plt.ylabel('minutes after 22:00')
plt.show()