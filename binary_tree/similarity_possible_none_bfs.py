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

def bfs(self):
  res = []
  if self.head is None:
      return res

  gen = [self.head]
  nex = []
  while gen:
      gl = []
      for g in gen:
          d = g.data if g is not None else g
          gl.append(d)
          
      res.append(gl)
      _gen_nex(gen, nex)
      gen = nex
      nex = []

  return res

def is_same(t1, t2):
    b1 = bfs(t1)
    b2 = bfs(t2)
    return b1 == b2

def _gen_nex(gen, nex):
    for n in gen:
        if n is None:
            continue

        nex.append(n.left)
        nex.append(n.right)
    
t1 = BinaryTree()
t2 = BinaryTree()
assert is_same(t1, t2) == True

t1 = BinaryTree()
t1.insert(10)

t2 = BinaryTree()
t2.insert(10)

assert is_same(t1, t2) == True

t1 = BinaryTree()
t1.insert(10)

t2 = BinaryTree()
t2.insert(20)

assert is_same(t1, t2) == False

t1 = BinaryTree()
for x in [4, 2, 6, 1, 3, 5, 7]:
    t1.insert(x)

t2 = BinaryTree()
for x in [4, 2, 6, 1, 3, 5, 7]:
    t2.insert(x)

assert is_same(t1, t2) == True

t1 = BinaryTree()
for x in [4, 2, 6, 1, 3, 5, 7]:
    t1.insert(x)

t2 = BinaryTree()
for x in [4, 2, 6, 1, 3, 5, 8]:
    t2.insert(x)

assert is_same(t1, t2) == False

t1 = BinaryTree()
for x in [5, 4, 3, 2]:
    t1.insert(x)

t2 = BinaryTree()
for x in [5, 4, 3, 2]:
    t2.insert(x)

assert is_same(t1, t2) == True

t1 = BinaryTree()
root = BinaryNode(1, None, None)
root.left = BinaryNode(2, None, None)
t1.head = root

t2 = BinaryTree()
root = BinaryNode(1, None, None)
root.right = BinaryNode(2, None, None)
t2.head = root

assert is_same(t1, t2) == False

t1 = BinaryTree()
root = BinaryNode(1, None, None)
root.left = BinaryNode(2, None, None)
root.right = BinaryNode(3, None, None)
t1.head = root

t2 = BinaryTree()
root = BinaryNode(1, None, None)
root.left = BinaryNode(2, None, None)
root.right = BinaryNode(3, None, None)
t2.head = root

assert is_same(t1, t2) == True

print("All tests passed!")
    b1 = bfs(t1)
    b2 = bfs(t2)
    return b1 == b2

def _gen_nex(gen, nex):
    for n in gen:
        if n is None:
            continue

        nex.append(n.left)
        nex.append(n.right)
    
