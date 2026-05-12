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

              if prev is not None and prev.data == curr.data:
                  raise Exception()
              prev = curr
              curr = curr.next

          print()

def reverse_linkedlist_2(ll, left, right):
    head = ll.head
    curr = head
    head_left = None
    head_right = None
    inn_left = None
    inn_right = None
    i = 0

    prev = None
    nexx = None
    while curr:
        # print(i, curr.data, "aa")

        if i == left - 1:
            head_left = curr
        if i == right + 1:
            head_right = curr
        if i == left:
            inn_left = curr
            # print(inn_left.data, "inleft")
        if i == right:
            inn_right = curr
            # print(inn_right.data, "innright")

        if i >= left and i <= right:
            # print(i, 'aaa')
            nexx = curr.next

            if prev is not None:
                curr.next = prev
            else:
                curr.next = head_left
            # print(curr.data, curr.next.data,  "ssaa2")
            

        # print(i, curr.data, curr.next.data, "maybe braek")
        if i == right + 1 or (i < right + 1 and prev is not None and nexx is None):
            # print(i, curr.data, "bb")
            if head_left is not None:
                head_left.next = inn_right
            if inn_left is not None:
                inn_left.next = head_right
            break

        if i >= left and i <= right:    
            prev = curr
            curr = nexx
            i += 1

        else:
            curr = curr.next
            i += 1

    if left == 0:
        ll.head = inn_right

ll = LinkedList()
for i in range(4):
    ll.add(i)
ll.print()

reverse_linkedlist_2(ll, 1, 2)
ll.print()

ll =LinkedList()
for i in range(3):
    ll.add(i)
ll.print()

reverse_linkedlist_2(ll, 1, 2)
ll.print()

ll =LinkedList()
for i in range(3):
    ll.add(i)
ll.print()

reverse_linkedlist_2(ll, 0, 2)
ll.print()

ll =LinkedList()
for i in range(3):
    ll.add(i)
ll.print()

reverse_linkedlist_2(ll, 0, 1)
ll.print()

reverse_linkedlist_2(ll, 1, 2)
ll.print()

reverse_linkedlist_2(ll, 0, 2)
ll.print()

reverse_linkedlist_2(ll, 1, 2)
ll.print()
