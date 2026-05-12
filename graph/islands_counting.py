def get_close(start, mat, height, width):
  sy, sx = start
  if sy - 1 >= 0:
      yield (sy-1, sx)

  if sy + 1 < height:
      yield (sy+1, sx)
    
  if sx - 1 >= 0:
      yield (sy,sx - 1)
  
  if sx + 1 < width:
      yield (sy,sx + 1)

def get_neighbors(start, mat, visited, height, width):
    for neigh in get_close(start, mat, height, width):
        ny, ns = neigh
        if mat[ny][ns] == 1 and neigh not in visited:
            yield neigh

from collections import deque
def bfs(start, mat, height, width, visited):
   
    queue = deque([start])
    while queue:
        n = queue.pop()

        for neig in get_neighbors(n, mat, visited, height, width):
            if neig not in visited:
                queue.append(neig)
                visited.add(neig)

        # raise Exception

def count_islands(mat):
    height = len(mat)

    if height == 0:
        return 0
    width = len(mat[0])

    pool = [(y, x) for y in range(height) for x in range(width) if mat[y][x] == 1]
    count = 0
    visited = set()
    for s in pool:
        if s not in visited:
            count += 1
            bfs(s, mat, height, width, visited)

    return count


count_islands([
    [1,1,0,0],
    [1,0,0,1],
    [0,0,1,1],
    [0,1,0,0]
])


# empty grid
assert count_islands([]) == 0
assert count_islands([[]]) == 0

# single cell
assert count_islands([[0]]) == 0
assert count_islands([[1]]) == 1

# single row
assert count_islands([[1,0,1,1,0]]) == 2

# single column
assert count_islands([[1],[0],[1],[1],[0]]) == 2

# 2x2
assert count_islands([[1,0],
                      [0,1]]) == 2

assert count_islands([[1,1],
                      [1,1]]) == 1

assert count_islands([[0,0],
                      [0,0]]) == 0

# separate islands
assert count_islands([[1,0,1],
                      [0,0,0],
                      [1,0,1]]) == 4

# one big island
assert count_islands([[1,1,1],
                      [1,1,1],
                      [1,1,1]]) == 1

# L-shaped island
assert count_islands([[1,0,0],
                      [1,1,0],
                      [0,0,0]]) == 1


assert count_islands([[1,0,1],
                      [0,1,0],
                      [1,0,1]]) == 5

assert count_islands([
    [1,1,0,0],
    [1,0,0,1],
    [0,0,1,1],
    [0,1,0,0]
]) == 3

assert count_islands([
    [1,1,0,1],
    [0,1,0,0],
    [1,0,1,1],
    [0,0,0,1]
]) == 4



# thin horizontal strips
assert count_islands([
    [1,1,1,1,1]
]) == 1

# thin vertical strips
assert count_islands([
    [1],
    [1],
    [1],
    [1]
]) == 1

# alternating pattern
assert count_islands([
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0]
]) == 6


assert count_islands([
    [1,1,0,0,0,1],
    [1,0,0,1,1,1],
    [0,0,1,0,0,0],
    [1,1,0,0,1,0],
    [0,0,0,1,1,1]
]) == 5