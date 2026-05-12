def abs(x):
  if x < 0:
      return -x
  return x

def sorted_squared_sorted(arr):
  if len(arr) == 0:
      return []

  # get index of 0 
  zidx = None
  for i in range(len(arr)): 
      if arr[i] >= 0:
          zidx = i
          break
  else:
      zidx = len(arr) - 1

  res = []
  l = zidx - 1
  r = zidx
  l1 = len(arr) - 1

  # print(zidx, "zidx")
  while l >= 0 and r <= l1:
      if abs(arr[l]) < abs(arr[r]):
          res.append(arr[l] * arr[l])
          l -= 1
      else:
          res.append(arr[r] * arr[r])
          r += 1

  while l >= 0:
      res.append(arr[l] * arr[l])
      l -= 1
    
  while r <= l1:
      res.append(arr[r] * arr[r])
      r += 1

  return res


assert sorted_squared_sorted([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert sorted_squared_sorted([-7, -3, -1]) == [1, 9, 49]
assert sorted_squared_sorted([0, 2, 5]) == [0, 4, 25]
assert sorted_squared_sorted([-5, -3, -2, -1]) == [1, 4, 9, 25]
assert sorted_squared_sorted([1, 2, 3, 4]) == [1, 4, 9, 16]
assert sorted_squared_sorted([0]) == [0]
assert sorted_squared_sorted([-1]) == [1]
assert sorted_squared_sorted([]) == []
assert sorted_squared_sorted([-2, -1, 0, 1, 2]) == [0, 1, 1, 4, 4]
assert sorted_squared_sorted([-10, -5, -2, 0, 1, 3]) == [0, 1, 4, 9, 25, 100]