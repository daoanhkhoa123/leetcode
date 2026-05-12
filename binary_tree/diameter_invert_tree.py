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

    def bfs(self):
        yield from self._bfs_internal(self.head)

    def _bfs_internal(self, p):
        yield p

        if p.left is not None:
            yield from self._bfs_internal(p.left)

        if p.right is not None:
            yield from  self._bfs_internal(p.right)

    def print(self):
        for n in self.bfs():
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

def diameter(tree):
    d = 0
    
    def depth(root):
        nonlocal d
        
        if root is None:
            return 0
        left = depth(root.left)
        right = depth(root.right)

        d = max(d, left + right)
        return 1 + max(left,  right)
    
    
    depth(tree.head)
    return d

def invert(tree):
    stack = Stack()
    if tree.head is None:
        return

    stack.push(tree.head)
    while not stack.is_empty():
        p = stack.pop()
        if p.left is not None:
            stack.push(p.left)
        if p.right is not None:
            stack.push(p.right)

        p.left, p.right = p.right, p.left
    return tree