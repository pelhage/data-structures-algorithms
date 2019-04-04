

def quickSort(arr, low, high):
	if low < high:
		split = partition(arr, low, high)
		quickSort(arr, low, split - 1)
		quickSort(arr, split + 1, high)

def partition(arr, start, end):
  pos = start
  for i in range(start, end):
    if arr[i] < arr[end]:
      arr[i],arr[pos] = arr[pos],arr[i]
      pos += 1
  arr[pos],arr[end] = arr[end],arr[pos]
  return pos


# a = [10,23,3,111,345,2,15]
# quickSort(a, 0, len(a) - 1)
# print a

# Sorts an array or list in ascending order using merge sort.
def mergeSort( theSeq ):
  n = len( theSeq )  
   # Create a temporary array for use when merging subsequences.
  tmpArray = [None]*n
   # Call the private recursive merge sort function.
  recMergeSort( theSeq, 0, n-1, tmpArray ) 
  
# Sorts a virtual subsequence in ascending order using merge sort. 
def recMergeSort( theSeq, first, last, tmpArray ):
 # The elements that comprise the virtual subsequence are indicated
 # by the range [first...last]. tmpArray is temporary storage used in
 # the merging phase of the merge sort algorithm.

   # Check the base case: the virtual sequence contains a single item.
  if first == last :
    return;
  else :
     # Compute the mid point.
    mid = (first + last) // 2   
    
     # Split the sequence and perform the recursive step.
    recMergeSort( theSeq, first, mid, tmpArray )
    recMergeSort( theSeq, mid+1, last, tmpArray )
    
     # Merge the two ordered subsequences.
    mergeVirtualSeq( theSeq, first, mid+1, last+1, tmpArray )

# Merges the two sorted virtual subsequences: [left..right) [right..end)
# using the tmpArray for intermediate storage.

def mergeVirtualSeq( theSeq, left, right, end, tmpArray ):
   # Initialize two subsequence index variables.
  a = left
  b = right  
   # Initialize an index variable for the resulting merged array.
  m = 0                                      
   # Merge the two sequences together until one is empty.
  while a < right and b < end :
    if theSeq[a] < theSeq[b] :
      tmpArray[m] = theSeq[a]
      a += 1
    else :
      tmpArray[m] = theSeq[b]
      b += 1
    m += 1
   
   # If the left subsequence contains more items append them to tmpArray.
  while a < right :
    tmpArray[m] = theSeq[a]
    a += 1
    m += 1
    
   # Or if right subsequence contains more, append them to tmpArray.
  while b < end :
    tmpArray[m] = theSeq[b]
    b += 1
    m += 1
   
   # Copy the sorted subsequence back into the original sequence structure.
  for i in range( end - left ) :
    theSeq[i+left] = tmpArray[i]  


# b = [10,23,3,111,345,2,15]
# mergeSort(b)
# print b


def bubbleSort(arr):
  for passnum in range(len(arr)-1,0,-1):
    for i in range(passnum):
      if arr[i] > arr[i+1]:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp

# c = [54,26,93,17,77,31,44,55,20]
# bubbleSort(c)
# print(c)

import random
import time

def compareSort():
  arr = []
  i = 1
  while i <= 1000:
    arr.append(random.randint(1, 100000))
    i += 1
  
  quickSortAvg = []
  bubbleSortAvg = []
  mergeSortAvg = []
  
  for ndx in range(0, 10):
    arr_quickSort = arr
    arr_mergeSort = arr
    arr_bubbleSort = arr

    qs_len = len(arr_quickSort) - 1
    time_before_quickSort = time.clock()
    quickSort(arr_quickSort, 0, qs_len)
    time_after_quickSort = time.clock()
    quickSortAvg.append(time_after_quickSort - time_before_quickSort)
    
    time_before_mergeSort = time.clock()
    mergeSort(arr_mergeSort)
    time_after_mergeSort = time.clock()
    mergeSortAvg.append(time_after_mergeSort - time_before_mergeSort)

    time_before_bubbleSort = time.clock()
    bubbleSort(arr_bubbleSort)
    time_after_bubbleSort = time.clock()
    bubbleSortAvg.append(time_after_bubbleSort - time_before_bubbleSort)

  print 'quickSort: {} s'.format(sum(quickSortAvg)/len(quickSortAvg))
  print 'mergeSort: {} s'.format(sum(mergeSortAvg)/len(mergeSortAvg))
  print 'bubbleSort: {} s'.format(sum(bubbleSortAvg)/len(bubbleSortAvg))

compareSort()
