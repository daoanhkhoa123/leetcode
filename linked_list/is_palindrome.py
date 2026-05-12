class LinkedNode:
    def __init__(self, data, next):
        self.data= data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = LinkedNode(data, None)

        if self.head is None:
            self.head = new_node

        else:
          curr = self.head
          while curr.next:
              curr = curr.next
          curr.next = new_node

    def print(self):
          print()
          curr = self.head
          prev = None
          while curr:
              print(curr.data, end=", ")

              # if prev is not None and prev.data == curr.data:
              #     raise Exception()
              prev = curr
              curr = curr.next

          print()

class Stack:
    def __init__(self) -> None:
        self.mem = []

    def add(self, x):
        self.mem.append(x)

    def pop(self):
        self.mem.pop()

    def peek(self, default= None):
        if not self.mem:
            return default
        return self.mem[-1]

    def print(self):
        print(self.mem)

def is_palidorme(ll):
    slow = ll.head
    fast = ll.head

    stack = Stack()

    while fast and fast.next:
        stack.add(slow.data)
        slow = slow.next
        fast = fast.next.next

    is_even = False
    if fast is None:
        is_even = True
    elif fast.next is None:
        is_even = False
    
    if not is_even:
        slow = slow.next

    # print(is_even, "even")
    
    # stack.print()
    # print(slow.data, slow.next.data, "nex")
    while slow:
        if slow.data == stack.peek():
            stack.pop()
        else:
            # print(slow.data, stack.peek(), "spe")
            return False

        slow = slow.next

    if stack.peek() is not None:
        return False
      
    return True

ll = LinkedList()
for i in [2, 5, 6, 7, 6, 7, 5, 2]:
    ll.add(i)
assert is_palidorme(ll) == False

ll = LinkedList()
for i in [2, 5, 7, 6, 7, 7, 6, 7, 5, 2]:
    ll.add(i)
assert is_palidorme(ll) == True


ll = LinkedList()
for i in [1, 2, 3, 2, 1]:
    ll.add(i)
assert is_palidorme(ll) == True

ll = LinkedList()
for i in [1]:
    ll.add(i)
assert is_palidorme(ll) == True

ll = LinkedList()
for i in []:
    ll.add(i)
assert is_palidorme(ll) == True

ll = LinkedList()
for i in [1, 2]:
    ll.add(i)
assert is_palidorme(ll) == False

ll = LinkedList()
for i in [1, 2, 3]:
    ll.add(i)
assert is_palidorme(ll) == False

ll = LinkedList()
for i in [1, 2, 2, 3]:
    ll.add(i)
assert is_palidorme(ll) == False