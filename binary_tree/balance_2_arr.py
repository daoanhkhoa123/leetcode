class BinaryNode:
    def __init__(self, data, left, right) -> None:
        self.data= data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = BinaryNode(data, None, None)
            return

        p = self.head
        while True:
            if data < p.data:
                if p.left is None:
                    p.left = BinaryNode(data, None, None)
                    break
                p = p.left

            else:
                if p.right is None:
                    p.right = BinaryNode(data, None, None)
                    break
                p = p.right

    def inorder(self):
        yield from self._inorder_internal(self.head)

    def _inorder_internal(self, p):

        if p.left is not None:
            yield from self._inorder_internal(p.left)

        yield p


        if p.right is not None:
            yield from  self._inorder_internal(p.right)

    def layer_by_layer(self):
        if self.head is None:
            return
        
        gen = [self.head]
        nex = []
        res = []
        while gen:
            res.append([g.data for g in gen])
            self._gen_nex(gen, nex)
            gen = nex
            nex = []
        return res

    def _gen_nex(self, gen, nex):
        for n in gen:
            if n.left is not None:
                nex.append(n.left)
            if n.right is not None:
                nex.append(n.right)

    def print(self):
        for n in self.inorder():
            print(n.data, end=", ")
        print()

class Stack:
    def __init__(self):
        self.mem = list()

    def push(self, x):
        self.mem.append(x)

    def pop(self):
        return self.mem.pop(-1)

    def peek(self):
        return self.mem[-1]

    def is_empty(self):
        return not self.mem

    def print(self):
        print(self.mem)

def from_sorted(arr):
    tree = BinaryTree()
    _from_sorted(tree, arr, 0, len(arr)-1)
    return tree

def _from_sorted(tree, arr, left, right):
    if left > right:
        return None
    
    mi = (left + right) // 2
    tree.insert(arr[mi])
    _from_sorted(tree, arr, left, mi - 1)
    _from_sorted(tree, arr, mi + 1, right)

def balance(tree):
    a = []
    for n in tree.inorder():
      a.append(n.data)
    return from_sorted(a)