""" 

manipulating vectors

inspired by practice exercises (with no solutions) in Deep Learning by: Andrew Trask, published by Grokking

jack nickelson

"""

import numpy as np

l1 = (2,3,4,5,6)
l2 = (9,8,7,6,5)

vec1 = np.array(l1)
vec2 = np.array(l2)

def dot_product(vec1,vec2):
    dprod = sum(vec1 * vec2)
    print("The dot product is: {}".format(dprod))

def vec_addition(vec1,vec2):
    vecadd = vec1 + vec2
    print("When adding the elements of each vector with the elements of a second vector, the resulting vector is: {}".format(vecadd))

def single_vec_sum(vec1):
    vecsum = sum(vec1)
    print("The sum of the vector is: {}".format(vecsum))

def single_vec_mean(vec1):
    vec_mean = sum(vec1)/len(vec1)
    print("The mean of the vector is: {}".format(vec_mean))


dot_product(vec1,vec2)
vec_addition(vec1,vec2)
single_vec_sum(vec1)
single_vec_mean(vec1)