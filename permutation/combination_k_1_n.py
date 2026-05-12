def combination_k_1_n(k, n):
    res = []      

    def backtrack(res, k, start, cache):
        if len(cache) == k:
            res.append(cache[:])
        if len(cache) > k:
            return

        for i in range(start, n + 1):
            cache.append(i)
            backtrack(res,k, i+1, cache)
            cache.pop()

    backtrack(res,k, 1, [])
    return res

combination_k_1_n(2, 4)