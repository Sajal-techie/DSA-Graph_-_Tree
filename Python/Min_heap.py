
class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        parent_index = (index - 1)//2
        if parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index
        if left < len(self.heap) and self.heap[smallest] > self.heap[left]:
            smallest = left
        if right < len(self.heap) and self.heap[smallest] > self.heap[right]:
            smallest = right
        if index != smallest:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)

    def delete(self, data):
        if len(self.heap) == 0:
            print("heap is empty")

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
            print("linked list is empty")
            return False
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def display(self):
        print(self.heap)



heap1 = MinHeap()
# heap1.insert(10)
# heap1.insert(6)
# heap1.insert(20)
# heap1.insert(25)
# heap1.insert(3)
# heap1.insert(8)
arr = [3,57,1,54,8,2,878,5]
for i in arr:
    heap1.insert(i)
heap1.display()
print(heap1.delete(200))
heap1.pop()
heap1.display()
