class Queue:
    def __init__(self):
        self.mem= []

    def pop(self):
        return self.mem.pop(0)

    def push(self, x):
        self.mem.append(x)

    def peek(self):
        return self.mem[0]

    def __len__(self):
        return len(self.mem)

    def is_empty(self):
        return not self.mem

    def print(self):
        print(self.mem)
      

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

def flipped_k_queue(q, k):
    lengq = len(q)
    s = Stack()
    for i in range(k):
        s.push(q.pop())

    while not s.is_empty():
        q.push(s.pop())

    for i in range(lengq-k):
        q.push(q.pop())

    return q

q = Queue()
for i in range(5):
    q.push(i)

flipped_k_queue(q, 5).print()