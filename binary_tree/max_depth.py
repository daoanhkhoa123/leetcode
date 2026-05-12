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

def max_depth(tree):
    depth = 0
    if tree.head is None:
        return depth

    gen = [tree.head]
    nex = []
    while gen:
        _gen_nex(gen, nex)
        gen = nex 
        nex = []
        depth += 1
    return depth

def _gen_nex(gen, nex):
    for n in gen:
        if n.left is not None:
            nex.append(n.left)
        if n.right is not None:
            nex.append(n.right)
    

tree = BinaryTree()
assert max_depth(tree) == 0

tree = BinaryTree()
tree.insert(10)
assert max_depth(tree) == 1

tree = BinaryTree()
root = BinaryNode(3, None, None)
root.left = BinaryNode(9, None, None)
root.right = BinaryNode(20, None, None)
root.right.left = BinaryNode(15, None, None)
root.right.right = BinaryNode(7, None, None)
tree.head = root
assert max_depth(tree) == 3

tree = BinaryTree()
for x in [4, 2, 6, 1, 3, 5, 7]:
    tree.insert(x)
assert max_depth(tree) == 3

tree = BinaryTree()
for x in [5, 4, 3, 2]:
    tree.insert(x)
assert max_depth(tree) == 4

tree = BinaryTree()
for x in [1, 2, 3, 4]:
    tree.insert(x)
assert max_depth(tree) == 4

tree = BinaryTree()
root = BinaryNode(1, None, None)
root.right = BinaryNode(2, None, None)
tree.head = root
assert max_depth(tree) == 2

tree = BinaryTree()
root = BinaryNode(1, None, None)
root.left = BinaryNode(2, None, None)
root.left.left = BinaryNode(3, None, None)
root.left.left.left = BinaryNode(4, None, None)
root.right = BinaryNode(5, None, None)
tree.head = root
assert max_depth(tree) == 4

print("All tests passed!")

tree = BinaryTree()
for i in [5, 4, 6,3, 8, 5]:
    tree.insert(i)
tree.print()
max_depth(tree)
