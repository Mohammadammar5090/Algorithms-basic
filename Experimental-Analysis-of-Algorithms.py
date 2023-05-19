from time import time
import matplotlib.pyplot as plt
import numpy as np
###FUN-1-
def prefix_average1(S):
    """Return list such that,
    for all j, A[j] equals average of S[0], ..., S[j].
    عمل لست من افرج الارقام نفسها
    """
    n = len(S)
    A = [0] * n  # create new list of n zeros
    for j in range(n):
        total = 0  # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
            A[j] = total / (j + 1)  # record the average
    return A

###FUN-2-
def prefix_average2(S):
    """Return list such that,
    for all j, A[j] equals average of S[0], ..., S[j].
    """
    n = len(S)
    A = [0]*n # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1) # record the average
    return A

###FUN-3-
def prefix_average3(S):
    """Return list such that,
    for all j, A[j] equals average of S[0], ..., S[j].
    """
    n = len(S)
    A = [0]*n # create new list of n zeros
    total = 0 # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j] # update prefix sum to include S[j]
        A[j] = total / (j+1) # compute average based on current sum
    return A

#a=[i for i in range(500)]


######################FUN-1-##########################
"""
start_time1 = time() # record the starting time

for i in range(1000):
     prefix_average1(a)

end_time1 = time() # record the ending time
elapsed1 = end_time1 - start_time1 # compute the elapsed time

elapsed1=elapsed1/1000
print(elapsed1)"""

######################FUN-2-##########################

"""
start_time2 = time() # record the starting time

for i in range(1000):
    prefix_average2(a)

end_time2 = time() # record the ending time
elapsed2 = end_time2 - start_time2 # compute the elapsed time
elapsed2=elapsed2/1000
print(elapsed2)"""

######################FUN-3-##########################

"""
start_time3 = time() # record the starting time

for i in range(1000):
    prefix_average3(a)

end_time3 = time() # record the ending time
elapsed3 = end_time3 - start_time3 # compute the elapsed time
elapsed3=elapsed3/1000

print(elapsed3)
"""


x = [50,100,200,400,500]
y1 = [0.00012554359436035156,0.0005182600021362304,0.0021144871711730956,0.008352859973907471,0.01589951968193054]
y2 = [2.3443937301635743e-05,7.515287399291992e-05 ,0.00024159455299377442 ,0.0008364284038543701,0.0012495601177215576]
y3 = [4.9350261688232426e-06,1.0735511779785156e-05,1.9561529159545898e-05 ,4.3880462646484375e-05,7.804250717163086e-05]
plt.plot(x, y1,"r")
plt.plot(x, y2,"b")
plt.plot(x, y3,"y")
plt.show()




