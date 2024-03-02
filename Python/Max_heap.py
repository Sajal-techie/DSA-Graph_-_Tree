class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        parent = (index - 1) // 2

        if parent >= 0 and self.heap[index] > self.heap[parent]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)

    def heapify_down(self, index):
        left_child = (index * 2) + 1
        right_child = (index * 2) + 2
        largest = index
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if index != largest:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

    def delete(self, data):
        if not self.heap:
            print('heap is empty')
            return False
        for i in range(len(self.heap)):
            if self.heap[i] == data:
                last = self.heap.pop()
                if i < len(self.heap):
                    self.heap[i] = last
                    self.heapify_down(i)
                return True
        return False

    def pop(self):
        if len(self.heap) == 0:
            print('empty heap')
            return False
        elif len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

    def display(self):
        print(self.heap)


heap2 = MaxHeap()
arr = [10,20,30, 15,11,2,5,1,3,8,9,22]
# arr = ['s','a','p','q','b','z']
for i in arr:
    heap2.insert(i)
heap2.display()
print(heap2.delete(2))
heap2.pop()
heap2.display()
