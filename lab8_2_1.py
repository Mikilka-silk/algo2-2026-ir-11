def count_paths(W, H, grid):
    sum_paths = {chr(i): 0 for i in range(97, 123)}

    prev_col = [1] * H

    for y in range(H):
        sum_paths[grid[y][0]] += 1

    for x in range(1, W):
        curr_col = [0] * H

        for y in range(H):
            char = grid[y][x]
            prev_char = grid[y][x-1]

            if char == prev_char:
                curr_col[y] = sum_paths[char]
            else:
                curr_col[y] = prev_col[y] + sum_paths[char]

        for y in range(H):
            char = grid[y][x]
            sum_paths[char] += curr_col[y]
        
        prev_col = curr_col
    
    if H == 1:
        return prev_col[0]
    else:
        return prev_col[0] + prev_col[H-1]