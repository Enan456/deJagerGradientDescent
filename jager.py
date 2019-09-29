import math
import system as sys
#arrays
personalNum = [246,92,57,1295]
target = 3096
jagerIndex = [-5,-4,-3,-2,-1,-1/2,-1/3,-1/4,0,1/4,1/3,1/2,1,2,3,4,5]
indicies = [8,8,8,8]
predictions = [1,1,1,1]
distance = sys.maxDouble

def arrFiller(arr):
    for i in arr:
        arr[i] = input()
    return arr

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
def arrCalc(pn,ind):
    distance = 1
    for i in pn:
        for j in ind:
            distance = distance * (i**j)
    return distance


for i in personalNum:
    for j in jagerIndex:
        indicies[i]=jagerIndex[j]
        

