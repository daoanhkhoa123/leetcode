def min_dei(arr):
    arr.sort()

    m = None
    res = []
    for i in range(1, len(arr)):
        x , y = arr[i-1], arr[i]
        if x > y:
            x, y = y, x
        d = y - x

        if m is not None and d > m:
            continue 

        elif m is None or d < m :
            res = [[x, y]]
            m = d

        elif d == m:
            res.append([x, y])

    return res

# Example cases
assert min_dei([4,2,1,3]) == [[1,2],[2,3],[3,4]]
assert min_dei([1,3,6,10,15]) == [[1,3]]
assert min_dei([3,8,-10,23,19,-4,-14,27]) == [[-14,-10],[19,23],[23,27]]

# Edge cases
assert min_dei([1,2]) == [[1,2]]
assert min_dei([2,1]) == [[1,2]]

# Already sorted
assert min_dei([1,2,3,4,5]) == [[1,2],[2,3],[3,4],[4,5]]

# Reverse sorted
assert min_dei([5,4,3,2,1]) == [[1,2],[2,3],[3,4],[4,5]]

# Large gaps
assert min_dei([1,100,200,300]) == [[1,100]]

# Negative numbers
assert min_dei([-5,-4,-3,-1]) == [[-5,-4],[-4,-3]]

# Mixed positive & negative
assert min_dei([-2,0,2,3]) == [[2,3]]

# Two minimum pairs only
assert min_dei([1,5,6,10]) == [[5,6]]

# Non-consecutive minimum repeats
assert min_dei([1,3,4,6,8]) == [[3,4]]

# Random order
assert min_dei([10,1,7,3,9]) == [[9,10]]