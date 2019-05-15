# Davis, David A    80610753

# For this lab asignment we weres asked to do 2 things. First to see if the two
# trigonometric functions are equivalent and the second task was to see if there
# is an existing partition between 2 subset of numbers. The main purpose of this
# lab assignment is to learn how different algorithms work. For this lab assign-
# ment we worked with randomization


import random
import numpy as np
from math import *
import time

def equal(f1, f2,tries=1000,tolerance=0.0001):
    srt = 100
    for i in range(tries):
        t = random.randrange(0, srt)
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True

def subsetsum(S,last,goal):
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last]) # Take S[last]
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]


# This method sees if the identities are equivalent to each other
def TrigoExpressions(L):
    
    for i in range(len(L)):
        for j in range(i + 1, len(L)):    
            if equal(L[i], L[j]) == True: # checks if they are equal 
                print(L[i], ' and ', L[j], ' are equivalent')
                print()

# this method checks if there's a partition in the subsets
def partition(L):

    if sum(L) % 2 == 0:  #check if inital sum is even
        
        total = sum(L)
        a,set1 = subsetsum(L, len(L) - 1, total / 2)  #get an inital subset
        set2 = []     #blank list for the remaining elements in the original list

        for i in range(len(L)):    
            if L[i] not in set1: # checks if it doesn't repeat       
                set2.append(L[i])        
        if sum(set1) != sum(set2):   # evaluate two sums
            return None
        return set1, set2
    
    else:
        return None  
    
identities = ['sin(t)', 'cos(t)', 'tan(t)',
        '-sin(t)','-cos(t)', '-tan(t)', 'sin(-t)',
        'cos(-t)', 'tan(-t)', 'sin(t)/cos(t)', '2*sin(t/2)*cos(t/2)',
        'sin(t) * sin(t)', '1-cos(2*t) * 1-cos(2*t)', '(1-cos(2*t)*1-cos(2*t))/2', '1/(cos(t))']

start1 = time.time()  
    
TrigoExpressions(identities)

print("--- %s seconds ---" % (time.time() - start1))
print()
print('----------------------------------------------------')
print()

# FOR SUBSET SUM


S = [2,4,12,5,9]        # this one shows the sets
#S = [2,6,8,12,20,30]   # this shows None

g = sum(S)
print('The sum of the numbers is: ',g)
start2 = time.time()
print(partition(S))
print("--- %s seconds ---" % (time.time() - start2))

