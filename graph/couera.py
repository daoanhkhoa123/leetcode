class Graph:
    def __init__(self):
        self.graph = {}

    def get_neigh(self, u):
        if u not in self.graph:
            return

        for n in self.graph[u]:
            yield n

    def get_vertex(self):
        v = set()
        for n in self.graph:
            for y in self.graph[n]:
                if y not in v:
                    v.add(y)
                    yield y

            if n not in v:
                v.add(n)
                yield n

    def add_edge(self, u, v, d=1):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = d

    def delete_vertex(self, v):
        for n in self.graph:
            if v in self.graph[n]:
                del self.graph[n][v]
        if v in self.graph:
            del self.graph[v]

    def bfs(self, start):
        visited = {start}
        queue = [start]
        while queue:
            n = queue.pop(0)
            for ne in self.get_neigh(n):
                if ne not in visited:
                    visited.add(ne)
                    queue.append(ne)
            yield n

    def dfs(self, start):
        visited = {start}
        stack = [start]
        while stack:
            n = stack.pop()
            for ne in self.get_neigh(n):
                if ne not in visited:
                    visited.add(ne)
                    stack.append(ne)
            yield n

    def __str__(self):
        return str(self.graph)

    def has_cycle(self, start):
        visited = set()
        stack = [(start, None)]

        while stack:
            v, p = stack.pop()

            if v in visited:
                return True
            visited.add(v)

            for ne in self.get_neigh(v):
                if ne != p:
                    stack.append((ne, v))
        return False


    def djakstra_lowest_cost(self, u, v):
        stack = [u]
        weights = {u:0}

        while stack:
            n = stack.pop()

            for v in self.get_neigh(n):
                stack.append(v)
                if v not in weights:
                    weights[v] = weights[n] + self.graph[n][v]
                else:
                    weights[v] = min(weights[v], weights[n] + self.graph[n][v])

        return weights[v]

    def cheapest_k_stop_bellman(self, src, dst, k):
        ws = {src:0}

        for i in range(k+1):
            t_ws = ws.copy()

            for v in self.get_vertex():
                if v not in ws:
                    continue

                for ne in self.get_neigh(v):
                    if ws[ne] > ws[v] + self.graph[v][ne]:
                        t_ws[ne] = ws[v] + self.graph[v][ne]
            ws = t_ws

        return ws.get(dst, -1)


def _get_no_parent(graph):
    v = set([key for d in graph.graph.values() for key in d.keys()])
    for n in graph.graph:
        if n not in v:
            return n 

    return None

def coursera(arr):
    g = Graph()
    for a in arr:
        x, y = a
        g.add_edge(y, x)


    while True:
        x = _get_no_parent(g)
        g.delete_vertex(x)

        if not g.graph:
            return True
        if x is None and g.graph:
            return False

assert coursera([]) == True

assert coursera([[1, 0]]) == True
assert coursera([[0, 1]]) == True

assert coursera([[1, 0], [2, 1], [3, 2]]) == True
assert coursera([[1, 0], [2, 0], [3, 1], [3, 2]]) == True

assert coursera([[1, 0], [0, 1]]) == False
assert coursera([[1, 0], [2, 1], [0, 2]]) == False

assert coursera([[1, 0], [2, 1], [3, 2], [1, 3]]) == False

assert coursera([[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]]) == True

assert coursera([[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [0, 5]]) == False

assert coursera([[2, 1], [4, 3]]) == True

assert coursera([[1, 1]]) == False
assert coursera([[0, 0]]) == False

assert coursera([[1, 0], [2, 1], [3, 2], [4, 2], [5, 4]]) == True

assert coursera([[1, 0], [2, 1], [3, 2], [4, 3], [2, 4]]) == False
