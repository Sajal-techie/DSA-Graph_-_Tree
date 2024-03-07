class Heap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def heapify_up(self, index):
        parent = (index - 1)//2
        if parent >= 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)

    def heapify_down(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if index!=largest:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)

    def insert(self, key, priority):
        data = key, priority
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)

    def pop(self):
        first = self.heap.pop(0)[1]
        self.heapify_down(0)
        return first


heap = Heap()
heap.insert(4, 100)
heap.insert(10,50)
heap.insert(7,150)
heap.insert(3,111)
heap.insert(6,99)
print(heap)
print(heap.pop())
print(heap.pop())
print(heap)