`class Heap:
    def __init__(self):
        self.mem = [0]
        self.size = 0

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


def get_kth_lar(arr, k):
    h = Heap.from_arr(arr[:k])

    for i in range(k, len(arr)):
        if arr[i] > h.get_min():
            h.pop_push(1, arr[i])

    return h.pop_min()