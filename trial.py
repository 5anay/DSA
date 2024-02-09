#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Data Structures and Algorithms 
arr = [2,6,7,5,4,8,3,9,1,0]


# In[20]:


# Insertion Sort: Like sorting cards that are in your hand as you pick them up from a table
def insertion_sort(arr):
    for j in range(0, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key

    print(arr)

insertion_sort(arr)


# In[21]:


#Selection Sort: 
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
            #Find the next minimum element in the rest of the sorting array
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(arr)

                            
selection_sort(arr)


# In[22]:


#Bubble Sort: Like bubbles, the larger values rise to the top, starting from the lowest index you move it down, moving the larger values up
def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(n-1,i-1,-1): # Starts at n-1 (since Python is 0-indexed), goes down to i (inclusive), stepping by -1
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    print(arr)

bubble_sort(arr)


# In[24]:


#Merge Sort
def mergeSort(arr):
    if len(arr) > 1:

        r = len(arr)//2
        leftArr = arr[:r]
        rightArr = arr[r:]

        mergeSort(leftArr)
        mergeSort(rightArr)

        i = j = k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1
    
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
            
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1

mergeSort(arr)
print(arr)


# In[25]:


#Quick Sort
def partition(A,l,h):
    pivot = A[l]
    i = l
    j = h
    while(i < j):
        while(A[i] <= pivot):
            i = i + 1 #i++ before the first check of A[i] <= pivot (do i++ while)
            while(A[j]>pivot):
                j = j - 1 #j-- before the first check of A[j] > pivot (do i++ while)
            if(i<j):
                A[i], A[j] = A[j], A[i]
        A[l], A[j] = A[j], A[l]
        return j

def quick_sort(A,l,h):
    if(l<h):
        j = partition(A,l,h)
        quick_sort(A,l,j)
        quick_sort(A,j+1, h)
    #print(A)
    
quick_sort(arr, 0, (len(arr)-1))
print(arr)


# In[27]:


#Heap Sort
def heapify(arr,l,r):
    print(arr)

def heap_sort(arr):
    print(arr)


# In[28]:


#Counting Sort
def counting_sort(A, k):
    #k = the largest element in A
    #B holds the sorted output 
    #C holds temporary working storage
    B = [0] * len(A)
    C = [0] * (k+1)
    
    #C[i] holds the number of input elements equal to i
    #C[0] holds the amount of 0s present in A
    #C[4] holds the amount of 4s present in A
    #for each integer i = 0,1,...,k 
    #where k is the largest value of the input array
    
    for j in range(len(A)):
        
        C[A[j]-1] = C[A[j]-1] + 1

    #C[i] now contains the number of elements less than 
    #or equal to i
    #C[3] is equal to amount of 0s,1s,2s,3s present in A
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]
        
    #for j in range(n-1,i-1,-1): # Starts at n-1 (since Python is 0-indexed), 
    #goes down to i (inclusive), stepping by -1
    #Place each element A[j] into its correct sorted position in the output arrayB
    #Because the elements might not be distinct, we decrement C[A[j]]ach time we place a value 
    #A[j] into the B array. Decrementing C[A[j]] causes the next input element with a value 
    #equal to A[j] if one exists, to go to the position immediately before A[j] in the output array.
    
    for j in range(0, len(B)):
        B[ C[ A[j] ] - 1] = A[j]
        C[ A[j] ] -= 1
    
    print(B)
        

counting_sort(arr, max(arr))


# In[29]:


#Stable Counting Sort
def stable_counting_sort(A, k):
    B = [0] * len(A)
    C = [0] * 10
    
    for j in range(len(A)):
        digit = (A[j] // 10**k) % 10
        C[digit] += 1

    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]

    for j in range(len(A)-1, -1, -1):
        digit = (A[j] // 10**k) % 10
        B[C[digit] - 1] = A[j]
        C[digit] -= 1
    
    print(B)
    return(B)

stable_counting_sort(arr, max(arr))


# In[30]:


#Radix Sort
def radix_sort(A):
    digit = max(A)
    count = 0

    while(digit > 0):
        digit = digit//10
        count = count + 1
        
    for i in range(count):
        A = stable_counting_sort(A,i)
        print(A)

    print(A)

radix_sort(arr)


# In[ ]:


#Tail Recursion vs Non-Tail recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

def fact_tail(n, accumulator=1):
    print(accumulator)
    if n == 0:
        return 1
    else:
        return fact_tail(n-1, accumulator*n)

fact_tail(1)

