# Name: Calvin Hicks
# Email: cahi0141@colorado.edu
# SUID: 810963108
#
from __future__ import print_function
import sys
import random
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
# --------- Insertion Sort -------------
# Implementation of getPosition
# Helper function for insertionSort
def getPosition(rList, elt):
    # Find the position where element occurs in the list
    #
    for (i,e) in enumerate(rList):
        if (e >= elt):
            return i
    return len(rList)

# Implementation of Insertion Sort 
def insertionSort(lst):
    n = len(lst)
    retList = []
    for i in lst:
        pos = getPosition(retList,i)
        retList.insert(pos,i)    
    return retList

#------ Merge Sort --------------
def mergeSort(lst):    
    # TODO: Implement mergesort here
    # You can add additional utility functions to help you out.
    # But the function to do mergesort should be called mergeSort
    if (len(lst) <= 1):
        return lst
    n = len(lst)
    list1 = lst[:n/2]
    list2 = lst[n/2:]
    srt1 = mergeSort(list1)
    srt2 = mergeSort(list2)
    return merge(srt1, srt2)
def merge(a,b):
    i=0
    j=0
    aLength = len(a)
    bLength = len(b)    
    c = []
    #print(a,b)
    while (aLength > (i)) | (bLength > (j)):
        if (i == aLength):
            c.append(b[j])
            j+=1
            #print c
        elif (j == bLength):
            c.append(a[i])
            i+=1
            #print c
        elif (a[i] > b[j]):
            c.append(b[j])
            j+=1
            #print c            
        elif (a[i] < b[j]):
            c.append(a[i])
            i+=1
            #print c
        elif(a[i] == b[j]):
            c.append(a[i])
            i+=1
            #print c
    return c
        
#------ Quick Sort --------------
def quickSort(lst):
    # TODO: Implement quicksort here
    # You may add additional utility functions to help you out.
    # But the function to do quicksort should be called quickSort
    #return lst
    if(lst == None):
        return lst
    if (len(lst) == 1):
        return lst
    if (checkAscendingSorted(lst,lst)):
        return lst  
    y = random.randint(0,len(lst)-1)
    x = lst[y]
    newList = lst[0:y]
    i = 1
    while(len(lst) > y + i ):
        newList.append(lst[y + i])
        i += 1
    lstLength = len(newList)
    i = 0
    lsSmall = []
    lsLarge = []
    while (lstLength > i):
        if (x <= newList[i]):
            lsLarge.append(newList[i])
            i += 1            
        elif (x > newList[i]):
            lsSmall.append(newList[i])   
            i += 1 
    lsSmall.append(x)
    lsSmall = quickSort(lsSmall)
    lsLarge = quickSort(lsLarge)
    i = 0
    while(len(lsLarge) > i):
        lsSmall.append(lsLarge[i])
        i += 1
    return lsSmall
    
def checkAscendingSorted(lstRet,lst):
    # Are they the same size
    if (len(lstRet) == len(lst)):
        # Is lstRet sorted?
        for i in range(0,len(lstRet)-1):
            if (lstRet[i] > lstRet[i+1]):
                return False
        # Is lstRet same as lst?
        for i in lst:
            if (i not in lstRet):
                return False
        for i in lstRet:
            if (i not in lst):
                return False
        return True
    else:
        return False
# ------ Timing Utility Functions ---------

# Function: generateRandomList
# Generate a list of n elements from 0 to n-1
# Shuffle these elements at random

def generateRandomList(n):
   # Generate a random shuffle of n elements
   lst = list(range(0,n))
   random.shuffle(lst)
   return lst


def measureRunningTimeComplexity(sortFunction,lst):
    t0 = time.clock()
    sortFunction(lst)
    t1 = time.clock() # A rather crude way to time the process.
    return (t1 - t0)


# --- TODO

# Write code to extract average/worst-case time complexity
dataMerge = []
dataQuick = []
dataInsertion = []
i = 0
while i < 50:
    lst = generateRandomList(1000*i)
    dataQuick.append(measureRunningTimeComplexity(quickSort,lst))
    dataInsertion.append(measureRunningTimeComplexity(insertionSort,lst))
    dataMerge.append(measureRunningTimeComplexity(mergeSort,lst))
    i+=1
    
quick = plt.plot(dataQuick, label = 'quickSort')
insert = plt.plot(dataInsertion, label = 'insertionSort')
mergesrt = plt.plot(dataMerge, label = 'mergeSort')
plt.setp(mergesrt, color='b', linewidth=2.0)
plt.setp(quick, color='r', linewidth=2.0)
plt.setp(insert, color='g', linewidth=2.0)
plt.ylabel('time complexity')
plt.xlabel('size of list')
plt.title('Sorting Algorithms Efficiency as List Size Increases')
plt.legend(loc = 2)
plt.show()

avgQuick = sum(dataQuick)
avgQuick = avgQuick/len(dataQuick)
print("average time for quick sort ",  avgQuick)

avgMerge = sum(dataMerge)  
avgMerge = avgMerge/len(dataMerge)
print("average time for merge sort ",  avgMerge)

avgInsrt = sum(dataInsertion)
avgInsrt = avgInsrt/len(dataInsertion)
print("average time for insertino sort ",  avgInsrt)
        
dataMerge = []
dataQuick = []
dataInsertion = []
i = 0

while i < 50:
    lst = generateRandomList(1000)
    dataQuick.append(measureRunningTimeComplexity(quickSort,lst))
    dataInsertion.append(measureRunningTimeComplexity(insertionSort,lst))
    dataMerge.append(measureRunningTimeComplexity(mergeSort,lst))
    i+=1

quick = plt.plot(dataQuick, label = 'quickSort')
insert = plt.plot(dataInsertion, label = 'insertionSort')
mergesrt = plt.plot(dataMerge, label = 'mergeSort')
plt.setp(mergesrt, color='b', linewidth=2.0)
plt.setp(quick, color='r', linewidth=2.0)
plt.setp(insert, color='g', linewidth=2.0)
plt.ylabel('time complexity')
plt.xlabel('list number')
plt.title('Sorting Algorithms Efficiency on Random Lists of Size 1000')
plt.legend(loc = 2)
plt.show() 
        
maxQuick = max(dataQuick)
print("max time for quick sort ",  maxQuick)

maxMerge = sum(dataMerge)  
print("max time for merge sort ",  maxMerge)

maxInsrt = max(dataInsertion)
print("max time for insertino sort ",  maxInsrt)
        