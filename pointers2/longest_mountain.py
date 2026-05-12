def longest_mountain(arr):
      p_state = 0
      state = 0
      s1 = -1
      s2 = -1
      res = 0
      has_p = False

      for i in range(1, len(arr)):
          if arr[i] > arr[i-1]:
              state = 1
          elif arr[i] < arr[i-1]:
              state = -1
          else:
              state = 0

              if p_state == 1:
                  s1 = -1
                  s2 = -1


          if p_state == 1 and state == -1:
              has_p = True
          if state == 1 and i == 1:
              s1 = 0

          if (p_state == -1 and (state == 1 or state == 0)) or ((p_state == 0 or p_state == -1) and state == 1):
              s2 = i - 1
              if s1 != -1 and has_p:
                  res = max(res, s2 - s1 + 1)
              # print(s1, s2, "aa")
              s1 = s2 

          if state == -1 and i == len(arr) - 1:
              s2 = i
              if s1 != -1 and has_p:
                  res = max(res, s2 - s1 + 1)

          p_state = state

      return res

# Example cases
assert longest_mountain([2,1,4,7,3,2,5]) == 5
assert longest_mountain([2,2,2]) == 0

# Minimal size
assert longest_mountain([]) == 0
assert longest_mountain([1]) == 0
assert longest_mountain([1,2]) == 0

# Simple mountain
assert longest_mountain([1,2,1]) == 3

# Strictly increasing (no descent)
assert longest_mountain([1,2,3,4,5]) == 0

# Strictly decreasing (no ascent)
assert longest_mountain([5,4,3,2,1]) == 0

# Plateau breaks mountain
assert longest_mountain([1,2,2,1]) == 0
assert longest_mountain([1,2,3,3,2,1]) == 0

# Multiple mountains → pick longest
assert longest_mountain([1,2,1,2,3,4,3,2,1]) == 7  # [1,2,3,4,3,2,1]

# Mountain at the start
assert longest_mountain([1,3,2,1,2,3]) == 4  # [1,3,2,1]

# Mountain at the end
assert longest_mountain([1,2,3,2,1]) == 5

# Complex case
assert longest_mountain([0,1,2,3,4,2,1,2,3,2,1]) == 7  # [0,1,2,3,4,2,1]

# Multiple small mountains
assert longest_mountain([1,2,1,2,1,2,1]) == 3

# Large flat regions
assert longest_mountain([1,1,1,2,3,2,1,1]) == 5

# Edge transitions
assert longest_mountain([1,2,3,2,1,0]) == 6
assert longest_mountain([0,1,2,3,2,1,0,1,2]) == 7

# Peaks with immediate drops
assert longest_mountain([1,3,2]) == 3
assert longest_mountain([2,5,3]) == 3

# Multiple equal peaks (invalid)
assert longest_mountain([1,2,3,3,3,2,1]) == 0
assert longest_mountain([1,2,3,2,2,1]) == 4

# Alternating slopes
assert longest_mountain([1,2,1,2,1,2,3,2,1]) == 5

# Long increasing then flat then decreasing
assert longest_mountain([1,2,3,4,4,4,3,2,1]) == 0

# Nested mountains
assert longest_mountain([1,2,3,2,1,2,3,2,1,0]) == 6

# Small fluctuations
assert longest_mountain([1,2,1,1,2,1]) == 3

# Peak at boundaries invalid
assert longest_mountain([3,2,1,2,3]) == 0

# Large valid mountain in noise
assert longest_mountain([5,5,1,2,3,4,3,2,1,6,6]) == 7

# Multiple plateaus inside
assert longest_mountain([1,2,2,3,4,3,2,1]) == 6

# Descend only at end
assert longest_mountain([1,2,3,4,3]) == 5

# Ascend only at start
assert longest_mountain([2,3,4,3,2,1]) == 6

# Repeated small peaks
assert longest_mountain([1,2,1,2,1,2,1,2,1]) == 3

# Long decreasing tail
assert longest_mountain([1,2,3,4,3,2,1,0,-1,-2]) == 10

# Multiple valid equal-length mountains
assert longest_mountain([1,2,3,2,1,2,3,2,1]) == 5

# Single valid mountain surrounded by flats
assert longest_mountain([0,0,1,2,3,2,1,0,0]) == 7

# Zigzag but no valid mountain
assert longest_mountain([1,2,1,2,2,1,2,1]) == 3

# Increasing, dip, then increasing (no full mountain)
assert longest_mountain([1,2,3,2,3,4,5]) == 4

# Decreasing, rise, decreasing (one valid)
assert longest_mountain([5,4,3,4,5,4,3,2]) == 6

# Very short valid segments
assert longest_mountain([0,1,0,1,0]) == 3

# Flat at peak invalid
assert longest_mountain([1,2,3,3,2,1]) == 0

# Flat at start then valid
assert longest_mountain([2,2,1,2,3,2,1]) == 5

# Flat at end then valid
assert longest_mountain([1,2,3,2,1,1,1]) == 5

# Large random-like
assert longest_mountain([3,1,2,3,4,3,2,1,2,3,2,1,0]) == 7

# Valley then mountain
assert longest_mountain([5,4,3,2,1,2,3,2,1]) == 5

# Multiple peaks but only one valid
assert longest_mountain([1,3,2,4,5,6,5,4,3,2,1]) == 9

# Plateau before ascent
assert longest_mountain([1,1,2,3,4,3,2,1]) == 7

# Plateau after descent
assert longest_mountain([1,2,3,4,3,2,1,1]) == 7

# All same except one bump
assert longest_mountain([2,2,2,3,2,2,2]) == 3

print("All tests passed!")
