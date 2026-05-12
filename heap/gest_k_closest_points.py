class Heap:
    def __init__(self):
        self.mem = [0]
        self.size = 0
        self.fn = None

    def __get_item__(self, key):
        if self.fn is not None:
            return self.fn(self.mem[key])

        return self.mem[key]

    def get_min(self):
        if self.size == 0:
            return None
        return self.mem[1]

    def insert(self, x):
        self.mem.append(x)
        self.size += 1
        self._perp_up(self.size)

    def pop_min(self):
        if self.size == 0:
            return None

        self.mem[1], self.mem[-1] = self.mem[-1], self.mem[1]
        res = self.mem.pop()
        self.size -= 1

        self._perp_down(1)
        return res

    def pop_push(self, i, v):
        res = self.mem[i]
        self.mem[i] = v

        if i * 2 <= self.size and v > self.mem[self._get_min_child_idx(i)]:
            self._perp_down(i)

        elif i//2 > 0 and (self.mem[i] < self.mem[i//2]):
            self._perp_up(i)
        return res

    def _perp_up(self, i):
        while i // 2 > 0:
            if self.mem[i] < self.mem[i//2]:
                self.mem[i], self.mem[i//2] = self.mem[i//2], self.mem[i]
            i //=2

    def _perp_down(self, i):
        while i * 2 <= self.size:
            mi = self._get_min_child_idx(i)
            if self.mem[i] > self.mem[mi]:
                self.mem[i], self.mem[mi] = self.mem[mi], self.mem[i]
            i = mi

    def _get_min_child_idx(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.mem[i*2] < self.mem[i*2+1]:
            return i *2
        return i* 2 + 1

    def print(self):
        print(self.mem)


    @classmethod
    def from_arr(cls, arr):
        size = len(arr)
        mem = [0] + arr

        h = cls()
        h.mem = mem
        h.size = size

        i = size // 2 + 1
        while (i:=i-1) > 0:
            h._perp_down(i)
        return h

def cal(a):
    return - a[0] ** 2 - a[1] ** 2

def get_k_closest(arr, k):
    h = Heap.from_arr([[cal(a), a] for a in arr[:k]])
    for i in range(k, len(arr)):
        d = cal(arr[i])
        if d > h.get_min()[0]:
            h.pop_push(1, [d, arr[i]])

    return [a[1] for a in h.mem[1:]]

  
assert sorted(get_k_closest([[1, 3], [-2, 2]], 1)) == sorted([[-2, 2]])

r = get_k_closest([[3, 3], [5, -1], [-2, 4]], 2)
assert sorted(r) == sorted([[3, 3], [-2, 4]])

assert sorted(get_k_closest([[0, 1], [1, 0]], 1)) in [
    sorted([[0, 1]]),
    sorted([[1, 0]])
]

r = get_k_closest([[1, 1], [2, 2], [3, 3]], 2)
assert sorted(r) == sorted([[1, 1], [2, 2]])

assert sorted(get_k_closest([[-1, -1], [2, 2], [0, 0]], 1)) == sorted([[0, 0]])

r = get_k_closest([[10, 10], [1, 1], [2, 2], [3, 3]], 3)
assert sorted(r) == sorted([[1, 1], [2, 2], [3, 3]])

assert sorted(get_k_closest([[5, 5]], 1)) == sorted([[5, 5]])

assert sorted(get_k_closest([[1, 2], [2, 1], [-1, -1]], 2)) in [
    sorted([[-1, -1], [1, 2]]),
    sorted([[-1, -1], [2, 1]])
]

r = get_k_closest([[4, 4], [0, 2], [2, 0], [1, 1]], 2)
assert sorted(r) in [
    sorted([[1, 1], [0, 2]]),
    sorted([[1, 1], [2, 0]])
]

assert sorted(get_k_closest([[1, 1], [2, 2]], 2)) == sorted([[1, 1], [2, 2]])