
def heapify_down(arr, n, index):
    left = (index * 2) + 1
    right = (index * 2) + 2
    largest = index
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify_down(arr,n,largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify_down(arr,n,i)
    print(arr)
    for i in range(n-1, 0 , -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_down(arr,i,0)

    return arr

arr = [1,3,6,5,99,11,77,55,88,12]
print(heapsort(arr))


