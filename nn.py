#!/usr/bin/env python

import numpy as np

#sigmoid function
def nonlin(x, deriv=False):
    if (deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

#input dataset gathering and processing
p = file('Warwick solver/msk_009.txt', 'r')
s = file('Warwick solver/msk_009.txt.solution', 'r')

currProblem = p.readline()
currSolution = s.readline()
intX = np.zeros( 81 ) #input
intY = np.zeros( 81 ) #output
X = np.empty( 324 ) #binary input
Y = np.empty( 324 ) #binary output

for i in range(81): #converts string to array of ints
    if currProblem[i] != '.': 
      intX[i] = int(currProblem[i])
    intY[i] = int(currSolution[i])

for i in range(81):
    temp = str(bin(int(intX[i]))[2:])
    temp2 = str(bin(int(intY[i]))[2:])
    while (len(temp) < 4):
        temp = "0" + temp
    while (len(temp2) < 4):
        temp2 = "0" + temp
    for k in range(4):
        X[4 * i + k] = temp[k]
        Y[4 * i + k] = temp2[k]
#tested and works up to here (input is clean)

np.random.seed(1) #seed random numbers to make calculation (deterministic)

#initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1

for iter in xrange(10000):

    #forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    #how much did we miss?
    l1_error = Y - l1

    #multiply how much we missed by the slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1, True)

    #update weights
    syn0 += np.dot(l0.T, l1_delta)

print "Output After Training:"
print l1


p.close()
s.close()
