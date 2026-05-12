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

from collections import Counter
def get_k_frequetest(arr, k):
    c = Counter(arr)
    c = [[v, k] for k, v in c.items()]

    h = Heap.from_arr(c[:k])
    for i in range(k, len(c)):
        if c[i][0] > h.get_min()[0]:
            h.pop_push(1, c[i])
    
    return [x[1] for x in h.mem[1:]]

assert sorted(get_k_frequetest([1, 1, 1, 2, 2, 3], 2)) == sorted([1, 2])

assert sorted(get_k_frequetest([1], 1)) == sorted([1])

assert sorted(get_k_frequetest([4, 4, 4, 6, 6, 7], 1)) == sorted([4])

assert sorted(get_k_frequetest([1, 2, 3, 4], 2)) in [
    sorted([1, 2]),
    sorted([1, 3]),
    sorted([1, 4]),
    sorted([2, 3]),
    sorted([2, 4]),
    sorted([3, 4])
]

assert sorted(get_k_frequetest([5, 5, 5, 5], 1)) == sorted([5])

assert sorted(get_k_frequetest([1, 2, 2, 3, 3], 2)) in [
    sorted([2, 3]),
    sorted([1, 2]),
    sorted([1, 3])
]

assert sorted(get_k_frequetest([-1, -1, -2, -2, -2, -3], 2)) == sorted([-2, -1])

assert sorted(get_k_frequetest([10, 20, 20, 30, 30, 30], 2)) == sorted([30, 20])

assert sorted(get_k_frequetest([7, 7, 8, 8, 9], 2)) in [
    sorted([7, 8]),
    sorted([7, 9]),
    sorted([8, 9])
]

assert sorted(get_k_frequetest([1, 1, 2, 2, 3, 3, 4], 3)) in [
    sorted([1, 2, 3]),
    sorted([1, 2, 4]),
    sorted([1, 3, 4]),
    sorted([2, 3, 4])
]