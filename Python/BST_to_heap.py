class BST:
    def __init__(self, data):
        self.key = data
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def inorder(self, heap):
        if self.lchild:
            self.lchild.inorder(heap)
        heap.append(self.key)
        if self.rchild:
            self.rchild.inorder(heap)

    def tree_to_heap(self):
        heap = []
        self.inorder(heap)
        n = len(heap)
        for i in range(n//2-1, -1, -1):
            self.heapify_up(i, heap)
        print(heap)

    def heapify_up(self, index, heap):
        parent = (index - 1)//2
        if parent >= 0 and heap[parent] > heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            self.heapify_up(parent, heap)


bst = BST(20)
arr = [62,6,7,2,54,9,3,1]
for i in arr:
    bst.insert(i)
bst.tree_to_heap()