def format_str(n_size, listed_pos):
    res = ""
    for col in listed_pos:
        first_len = col
        second_len = n_size - 1 - col
        res += "".join("."*first_len + "Q" +"."*second_len + "\n")

    return res

def solve_n_queens(n_size, fixed_queen):
    fixed_row = fixed_queen[0]
    fixed_col = fixed_queen[1]
    listed_pos = [-1] * n_size
    listed_pos[fixed_row] = fixed_col

    res = cal_recursive(listed_pos, 0, fixed_row)
    if res:
        return format_str(n_size, listed_pos)

    return None

def check_not_valid(r1, r2, c1, c2):
    return abs(r1 - r2) == abs(c1 - c2) or c1 == c2

def cal_recursive(listed_pos, cur_row, fixed_row):
    n_size = len(listed_pos)
    # print(n_size, listed_pos, cur_row, fixed_row)

    if cur_row == n_size:
        return True

    if cur_row == fixed_row:
        return cal_recursive( listed_pos, cur_row + 1, fixed_row) # next

    for col in range(n_size):
        if cur_row <= fixed_row:
          if check_not_valid(cur_row, fixed_row, col, listed_pos[fixed_row]):
              continue

        for i in range(cur_row):
            if check_not_valid(cur_row, i, col, listed_pos[i]):
                break

        else:
            # cur_row, col passed the tests
            listed_pos[cur_row] = col
            res = cal_recursive( listed_pos, cur_row + 1, fixed_row) # next
            if not res:
                listed_pos[cur_row] = -1
            else:
                return True
    return False

