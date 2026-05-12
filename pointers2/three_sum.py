def three_sum(arr):
    res = []
    arr.sort()

    # print(arr)
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i + 1
        right = len(arr) - 1
        # print(i, "ca")
        while left <  right: 

            sum = arr[i] + arr[left] + arr[right]
            # print(left, right,  sum, "aa")

            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                while left < right and arr[left - 1] == arr[left]:
                      left += 1
                # print(left, right, "e")
                # raise Exception()

    return res

def normalize(result):
    # sort each triplet and then sort the whole list
    return sorted([sorted(triplet) for triplet in result])


# ===== BASIC TESTS =====
assert normalize(three_sum([-1, 0, 1, 2, -1, -4])) == normalize([
    [-1, -1, 2],
    [-1, 0, 1]
])

assert normalize(three_sum([0, 1, 1])) == normalize([])

assert normalize(three_sum([0, 0, 0])) == normalize([
    [0, 0, 0]
])


# ===== EDGE CASES =====
assert normalize(three_sum([])) == normalize([])

assert normalize(three_sum([1])) == normalize([])

assert normalize(three_sum([1, 2])) == normalize([])


# ===== ALL NEGATIVE / POSITIVE =====
assert normalize(three_sum([-5, -4, -3, -2])) == normalize([])

assert normalize(three_sum([1, 2, 3, 4])) == normalize([])


# ===== MULTIPLE VALID TRIPLETS =====
assert normalize(three_sum([-2, 0, 1, 1, 2])) == normalize([
    [-2, 0, 2],
    [-2, 1, 1]
])

assert normalize(three_sum([-2, -1, 0, 1, 2, 3])) == normalize([
    [-2, -1, 3],
    [-2, 0, 2],
    [-1, 0, 1]
])


# ===== DUPLICATE HANDLING =====
assert normalize(three_sum([-1, -1, -1, 2, 2])) == normalize([
    [-1, -1, 2]
])

assert normalize(three_sum([0, 0, 0, 0])) == normalize([
    [0, 0, 0]
])


# ===== MIXED COMPLEX =====
assert normalize(three_sum([3, -2, 1, 0])) == normalize([])

assert normalize(three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2])) == normalize([
    [-4, 2, 2],
    [-2, 0, 2]
])