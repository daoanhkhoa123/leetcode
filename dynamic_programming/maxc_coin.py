def maxc(coin, sum):
    resu = sum % coin

    if resu != 0:
        return sum // coin, True
    return sum//coin, False
      
def maxc2(coins, sum, idx):
    base, has_resu = maxc(coins[idx], sum)

    if not has_resu:
        return base
    elif idx == 0:
        return None
    
    minn = None
    for b in range(base, -1, -1):
        rm = maxc2(coins, sum - b * coins[idx], idx - 1)
        if rm is not None:
            t = b + rm
            if minn is None or minn > t:
                minn = t


    return minn

def max_coin(coins, sum):
    if len(coins) == 0:
        if sum > 0:
            return -1
        elif sum == 0:
            return 0

    coins.sort()
    res = maxc2(coins, sum, len(coins) -1)
    if res is None:
        return -1
    return res



# Example cases
assert max_coin([1,2,5], 11) == 3
assert max_coin([2], 3) == -1
assert max_coin([1], 0) == 0

# Basic cases
assert max_coin([1], 1) == 1
assert max_coin([1], 2) == 2
assert max_coin([2,5,10], 0) == 0

# Impossible cases
assert max_coin([3,7], 5) == -1
assert max_coin([4,6], 3) == -1

# Multiple combinations
assert max_coin([1,3,4], 6) == 2   # 3+3
assert max_coin([1,3,4], 7) == 2   # 3+4
assert max_coin([2,5,10,1], 27) == 4  # 10+10+5+2

# Greedy fail cases
assert max_coin([1,4,5], 8) == 2   # 4+4
assert max_coin([1,3,4], 5) == 2   # 3+2? actually 1+4

# Large coin values
assert max_coin([186,419,83,408], 6249) == 20

# Single coin type
assert max_coin([7], 49) == 7
assert max_coin([7], 50) == -1

# Unsorted input
assert max_coin([5,1,2], 11) == 3

# Edge
assert max_coin([], 0) == 0
assert max_coin([], 1) == -1
assert max_coin([1], 0) == 0
assert max_coin([1], 1) == 1