def power_set(arr):
    res = []
    def backtrack(res, start, cache):
        res.append(cache[:])

        for i in range(start, len(arr)):
            cache.append(arr[i])
            backtrack(res, i + 1, cache)
            cache.pop()

    backtrack(res, 0, [])
    return res

power_set([1,2,3])