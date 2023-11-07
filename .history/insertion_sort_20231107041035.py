from timeit import default_timer as timer
import random 
#here we start the timer in order to analyze the time of this insertion algorithm
start = timer()
def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j>0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
#this is to generate random numbers
arr = []
for a in range(1,5):
    n = random.randint(1,5)
    arr.append(n)
#this is to generate the array in increasing order(best case)
array = sorted(arr)
#this is to generate an array in decreasing order
print(arr)    
insertion_sort(array)
print(array)
end = timer()
print(end-start)