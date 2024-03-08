class Minheap:
    def __init__(self):
        self.heap = []

    def heapify(self, index):
        left = (index*2)+1
        right = (index*2)+2
        smallest = index
        if left< len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if index!=smallest:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)

    def __str__(self):
        return str(self.heap)

    def insert(self, data):
        self.heap.append(data)
        self.heapify(0)

    def kth_largest(self, arr, k):
        for i in arr[:k]:
            self.insert(i)
        print(self)
        for i in arr[k:]:
            if i > self.heap[0]:
                self.heap.pop(0)
                self.insert(i)
        print(self)
        return self.heap[0]


k = 3
arr = [3,2,1,5,6,4,1000]
obj = Minheap()
print(obj.kth_largest(arr,k))