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

def average_level(tree):
    if tree.head is None:
        return []
    res = []
    gen=[tree.head]
    nex=[]
    while gen:
        avg = _averge(tree, gen, nex)
        res.append(avg)
        gen = nex 
        nex = []

    return res

def _averge(tree, gen, nex):
    avg = 0
    for n in gen:
        if n.left is not None:
            nex.append(n.left)
        if n.right is not None:
            nex.append(n.right)
        avg += n.data
    
    return avg/len(gen)

tree = BinaryTree()
for i in [5, 4, 6,3, 8, 5]:
    tree.insert(i)
tree.print()

average_level(tree)

def test_average_level_empty_tree():
    tree = BinaryTree()

    assert average_level(tree) == []


def test_average_level_single_node():
    tree = BinaryTree()
    tree.insert(10)

    assert average_level(tree) == [10.0]


def test_average_level_example_case():
    """
            3
          /   \
         9     20
              /  \
             15   7

    Level averages:
    [3, (9+20)/2, (15+7)/2]
    => [3.0, 14.5, 11.0]
    """

    # Build manually because insert() creates BST order
    tree = BinaryTree()

    root = BinaryNode(3, None, None)
    root.left = BinaryNode(9, None, None)
    root.right = BinaryNode(20, None, None)
    root.right.left = BinaryNode(15, None, None)
    root.right.right = BinaryNode(7, None, None)

    tree.head = root

    assert average_level(tree) == [3.0, 14.5, 11.0]


def test_average_level_balanced_tree():
    """
            4
          /   \
         2     6
        / \   / \
       1  3  5  7

    Averages:
    [4, 4, 4]
    """

    tree = BinaryTree()

    for x in [4, 2, 6, 1, 3, 5, 7]:
        tree.insert(x)

    assert average_level(tree) == [4.0, 4.0, 4.0]


def test_average_level_left_skewed():
    """
        5
       /
      4
     /
    3
   /
  2
    """

    tree = BinaryTree()

    for x in [5, 4, 3, 2]:
        tree.insert(x)

    assert average_level(tree) == [5.0, 4.0, 3.0, 2.0]


def test_average_level_right_skewed():
    """
    1
     \
      2
       \
        3
         \
          4
    """

    tree = BinaryTree()

    for x in [1, 2, 3, 4]:
        tree.insert(x)

    assert average_level(tree) == [1.0, 2.0, 3.0, 4.0]


def test_average_level_negative_values():
    """
            0
          /   \
        -10    10
        /        \
      -20         20

    Averages:
    [0, 0, 0]
    """

    tree = BinaryTree()

    root = BinaryNode(0, None, None)
    root.left = BinaryNode(-10, None, None)
    root.right = BinaryNode(10, None, None)
    root.left.left = BinaryNode(-20, None, None)
    root.right.right = BinaryNode(20, None, None)

    tree.head = root

    assert average_level(tree) == [0.0, 0.0, 0.0]

test_average_level_empty_tree()
test_average_level_single_node()
test_average_level_example_case()
test_average_level_balanced_tree()
test_average_level_left_skewed()
test_average_level_right_skewed()
test_average_level_negative_values()

print("All tests passed!")