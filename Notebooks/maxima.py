# Advanced Scientific Programming in Python, autumn school, Trento, 2010
# Day 1, Exercise 1 (unit testing and coverage)
# Author: Pietro Berkes <berkes _at_ brandeis _dot_ edu>
# Awfulized by Juan Luis Cano

def find_maxima(x):
	idx=[]
	N=  len(x)
	for i in range(N)  :    
    
    
    
        if x[i-1  ]<x[i] and x[i+1]<x[i]: idx.append(i)
        
        
    return idx
