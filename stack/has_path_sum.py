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


def has_path_sum(tree, s):
    stack  = Stack()
    if tree.head is None:
        return False

    stack.push((tree.head, tree.head.data))
    while not stack.is_empty():
        p, v = stack.pop()
        if p.left is None and p.right is None and v == s:
            return True
        
        if p.left is not None:
            stack.push((p.left, v + p.left.data))

        if p.right is not None:
            stack.push((p.right, v + p.right.data))

    return False