def heapify(arr, n, i):
 
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
   
    if l < n and arr[l] > arr[largest]:
        largest = l
 
    
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 
    
        heapify(arr, n, largest)
 
# Function to build a Max-Heap from the given array
def buildHeap(arr, n):
 
    startIdx = n // 2 - 1
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)
 
def printHeap(arr, n):
    print("Array representation of Heap is:")
 
    for i in range(n):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
 
    arr = list(map(int,input().split()))
    n = len(arr)
    buildHeap(arr, n)
 
    printHeap(arr, n)
 
   
 