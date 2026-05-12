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

def get_ope(s, a, b):
    if s == "+":
        return a + b
    if s == "*":
        return a * b
    if s == "-":
        return a - b    
    if s == "/":
        return int(a/b)

def isnumeric2(s):
    return s.isnumeric() or (s[0]=="-" and s[1:].isnumeric())

def polish_notation(a):
    stack = Stack()
    for c in a:
        if isnumeric2(c):
            stack.push(int(c))

        else:
            a = stack.pop()
            b = stack.pop()
            stack.push(get_ope(c, b, a))

    return stack.pop()

assert polish_notation(["2", "1", "+", "3", "*"]) == 9
assert polish_notation(["4", "13", "5", "/", "+"]) == 6
assert polish_notation(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
assert polish_notation(["3", "4", "+"]) == 7
assert polish_notation(["5", "1", "2", "+", "4", "*", "+", "3", "-"]) == 14
assert polish_notation(["7"]) == 7
assert polish_notation(["2", "3", "*", "5", "+"]) == 11
assert polish_notation(["8", "2", "/"]) == 4
assert polish_notation(["8", "3", "/"]) == 2
assert polish_notation(["18", "4", "-"]) == 14
assert polish_notation(["2", "3", "+", "4", "5", "+", "*"]) == 45
assert polish_notation(["15", "7", "1", "1", "+", "-", "/", "3", "*", "2", "1", "1", "+", "+", "-"]) == 5