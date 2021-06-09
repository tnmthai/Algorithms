# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 12:45:41 2021

@author: Thai Tran
"""
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        print ('j',j,i)
        if arr[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            print ('1',i,j, arr[i], arr[j])
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    print ('2',i+1, high, arr[i+1], arr[high])
    print ('3',i+1)
    return (i+1)
  
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
  
# Function to do Quick sort
  
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  
  
# Driver code to test above
arr = [10, 7, 8]
n = len(arr)

partition(arr, 0, n-1)

# quickSort(arr, 0, n-1)
# print("Sorted array is:")
# for i in range(n):
#     print("%d" % arr[i]),
  
