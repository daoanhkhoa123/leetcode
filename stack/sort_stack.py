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

def sort_stack(stack):
    tmp = Stack()
    tmp2 = Stack()
    while not stack.is_empty():
        x = stack.pop()

        if tmp.is_empty() or tmp.peek() < x:
            tmp.push(x)
        else:
            while not tmp.is_empty() and tmp.peek() > x:
                tmp2.push(tmp.pop())
            
            tmp.push(x) 
            while not tmp2.is_empty():
                tmp.push(tmp2.pop())

    return tmp

a = Stack()

for i in [5,2,3,1]:
    a.push(i)

sort_stack(a).print()