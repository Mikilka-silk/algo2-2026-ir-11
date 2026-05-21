def flood_fill(grid: list[list[str]], row: int, col: int, replacement: str) -> list[list[str]]:
    rows = len(grid)
    cols = len(grid[0])
    target_color = grid[row][col]

    if target_color == replacement:
        return grid

    queue = [(row, col)]
    grid[row][col] = replacement
    head = 0  

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while head < len(queue):
        r, c = queue[head]
        head += 1  
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == target_color:
                grid[nr][nc] = replacement
                queue.append((nr, nc))

    return grid


def parse_input(filename: str):
    with open(filename, 'r', encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    height, width = map(int, lines[0].split(","))

    row, col = map(int, lines[1].split(","))

    replacement = lines[2].strip("'\"")

    grid = []
    for line in lines[3:]:
        row_data = eval(line)
        grid.append(list(row_data))

    return grid, row, col, replacement, height, width


def write_output(filename: str, grid: list[list[str]]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for row in grid:
            f.write(str(row) + "\n")


if __name__ == "__main__":
    grid, start_row, start_col, replacement, _, _ = parse_input("input.txt")
    result = flood_fill(grid, start_row, start_col, replacement)
    write_output("output.txt", result)
    print("Результат збережено у output.txt")
    for row in result:
        print(row)
