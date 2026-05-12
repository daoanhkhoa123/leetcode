def climibng_star(n):
    a1 = 1
    a2 = 2

    if n <= 1:
        return a1
    if n == 2:
        return a2

    res = 0
    for i in range(3, n+1, 1):
        res = a1 + a2
        a1 = a2
        a2 = res
    return res

assert climibng_star(1) == 1
assert climibng_star(2) == 2
assert climibng_star(3) == 3
assert climibng_star(4) == 5
assert climibng_star(5) == 8
assert climibng_star(6) == 13
assert climibng_star(7) == 21
assert climibng_star(8) == 34
assert climibng_star(9) == 55
assert climibng_star(10) == 89

# edge cases
assert climibng_star(0) == 1  # if defined as 1 way (stay at ground)