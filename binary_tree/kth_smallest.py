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

    def get_max(self, root):
        while root.right:
            root = root.right
        return root
    
    def get_min(self, root):
        while root.left:
            root = root.left
        return root

    def _delete(self, p, d):
        while p:
          if p.data > d:
              p.left = self._delete(p.left, d)
          elif p.data < d:
              p.right = self._delete(p.right, d)
          else:
              if p.left is None:
                  return p.right
              elif p.right is None:
                  return p.left
              else:
                  p.data = self.get_min(p.right).data
                  p.right = self._delete(p.right, p.data)
          return p

    def delete(self, d):
        self._delete(self.head, d)
              

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


def kth_smallest(tree, k):
    for i, n in enumerate(tree.inorder()):
        if i == k-1:
            return n.data
          