def move_one_sprial(mat, width, height, start_y, start_x):
    for i in range(start_x, start_x + width + 1):
        yield mat[start_y][i]
    start_x = start_x + width

    for i in range(start_y + 1, start_y + height + 1):
        yield mat[i][start_x]
    start_y = start_y + height

    if height > 0:
        for i in range(start_x - 1, start_x - width - 1, -1):
            yield mat[start_y][i]
        start_x = start_x - width

    if width > 0:
        for i in range(start_y - 1, start_y - height, -1):
            yield mat[i][start_x]

def spiral_matrix(mat):
    if len(mat) == 0:
        return []

    height_offset = len(mat) - 1
    width_offset = len(mat[0]) - 1
    if height_offset == 0 and width_offset == 0:
        return mat[0]

    res = []
    start_y = 0
    start_x = 0
    while not (height_offset < 0 or width_offset < 0):
        res += [*move_one_sprial(mat, width_offset, height_offset, start_y, start_x)]

        height_offset -= 2
        width_offset -= 2
        start_x += 1
        start_y += 1

    return res

mat = [[1,2,3, 4],
       [5,6,7,8],
       [9,10,11,12]]

print(spiral_matrix(mat))

# 1x1
assert spiral_matrix([[1]]) == [1]

# 1xN (single row)
assert spiral_matrix([[1, 2, 3, 4]]) == [1, 2, 3, 4]

# Nx1 (single column)
assert spiral_matrix([[1], [2], [3], [4]]) == [1, 2, 3, 4]

# 2x2
assert spiral_matrix([[1, 2],
                      [3, 4]]) == [1, 2, 4, 3]

# 2x3
assert spiral_matrix([[1, 2, 3],
                      [4, 5, 6]]) == [1, 2, 3, 6, 5, 4]

# 3x2
assert spiral_matrix([[1, 2],
                      [3, 4],
                      [5, 6]]) == [1, 2, 4, 6, 5, 3]

# 3x3
assert spiral_matrix([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

# 3x4
assert spiral_matrix([[1,  2,  3,  4],
                      [5,  6,  7,  8],
                      [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

# 4x3
assert spiral_matrix([[1,  2,  3],
                      [4,  5,  6],
                      [7,  8,  9],
                      [10, 11, 12]]) == [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]

# 4x4
assert spiral_matrix([[1,  2,  3,  4],
                      [5,  6,  7,  8],
                      [9, 10, 11, 12],
                      [13,14, 15,16]]) == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

# rectangular (wide)
assert spiral_matrix([[1,2,3,4,5],
                      [6,7,8,9,10]]) == [1,2,3,4,5,10,9,8,7,6]

# rectangular (tall)
assert spiral_matrix([[1,2],
                      [3,4],
                      [5,6],
                      [7,8],
                      [9,10]]) == [1,2,4,6,8,10,9,7,5,3]

# with negatives
assert spiral_matrix([[0, -1, -2],
                      [-3, -4, -5]]) == [0, -1, -2, -5, -4, -3]

# non-square larger
assert spiral_matrix([[ 1,  2,  3,  4,  5],
                      [ 6,  7,  8,  9, 10],
                      [11, 12, 13, 14, 15],
                      [16, 17, 18, 19, 20]]) == [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]

# edge: empty matrix
assert spiral_matrix([]) == []

# edge: matrix with empty row
assert spiral_matrix([[]]) == []


# repeated values
assert spiral_matrix([[1,1,1],
                      [1,1,1]]) == [1,1,1,1,1,1]

# large thin
assert spiral_matrix([[i] for i in range(50)]) == list(range(50))

# large flat
assert spiral_matrix([list(range(50))]) == list(range(50))

# tricky inner loop
assert spiral_matrix([
    [1, 2, 3],
    [4, 5, 6]
]) == [1,2,3,6,5,4]

# hollow-ish pattern
assert spiral_matrix([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])[-2:] == [6,7]  # catches inner traversal mistakes