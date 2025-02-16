from random import choice
from numpy import array,dot,random
import numpy as np

#MCNeuron for And

w = random.rand(2)
w[1] = 1
w[0]=1
training_data = [
(array([0,0]),0),
(array([0,1]),0),
(array([1,0]),0),
(array([1,1]),1),
]

step_function = lambda x:0 if x< 2 else 1


for x, _ in training_data:
    result = dot(x,w)
print("{}:{} -> {}".format(x[:2],result,step_function(result)))
