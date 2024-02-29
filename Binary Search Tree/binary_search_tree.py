class BST:
    def __init__(self, data):
        self.key = data
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
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

    def search(self, data):
        if self.key == data:
            print("node is found in the tree")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node is not in tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not found in tree")

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

    def delete(self, data, curr):
        if self.key is None:
            print("empty tree")
            return
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("element is not on tree")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("this element is not in this tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                    return

                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                    return

                self = None
                return temp
            node = self.rchild
            while node.lchild is not None:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self

    def count(self, node):
        if node is None:
            return 0
        return 1 + self.count(node.lchild) + self.count(node.rchild)

    def min(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("smalled element is ", current.key)

    def max(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("largest element is ", current.key)

    def closest(self, data):
        closest = self.key
        current = self
        while current:
            if abs(current.key - data) < abs(closest - data):
                closest = current.key
            if data < current.key:
                current = current.lchild
            elif data > current.key:
                current = current.rchild
            else:
                return current.key
        return closest

    def isBST(self, node, min_value=float("-inf"), max_value=float("inf")):
        if node is None:
            return True

        if min_value < node.key < max_value:
            return self.isBST(node.lchild, min_value, node.key) and self.isBST(node.rchild, node.key, max_value)
        else:
            return False


tree = BST(10)
arr = [7,6,3,1,5,12]
for i in arr:
    tree.insert(i)
print(tree.count(tree))
tree.search(9)
tree.preorder()
print()
tree.inorder()
print()
tree.postorder()
print()
if tree.count(tree) > 1:
    tree.delete(1, tree.key)
else:
    print('only root node cant delete')
tree.preorder()
print()
tree.inorder()
print()
tree.postorder()
print()
tree.min()
tree.max()
print(tree.closest(9.3))
print(tree.isBST(tree))