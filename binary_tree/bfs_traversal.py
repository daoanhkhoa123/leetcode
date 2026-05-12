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
      res.append([g.data for g in gen])
      _gen_nex(gen, nex)
      gen = nex
      nex = []

  return res

def _gen_nex(gen, nex):
    for n in gen:
        if n.left is not None:
            nex.append(n.left)
        if n.right is not None:
            nex.append(n.right)
    
