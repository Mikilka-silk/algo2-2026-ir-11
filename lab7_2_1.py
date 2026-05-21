import csv

def matrix_reader(file_path):
    matrix = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            matrix.append([int(x) for x in row])
    return matrix

def prim_mst(matrix):
    n = len(matrix)
    if n == 0:
        return 0
    
    selected = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    total_weight = 0

    for _ in range(n):
        u = -1
        for v in range(n):
            if not selected[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v

        if u == -1 or min_edge[u] == float('inf'):
            break

        selected[u] = True
        total_weight += min_edge[u]

        for v in range(n):
            if matrix[u][v] > 0 and not selected[v]:
                if matrix[u][v] < min_edge[v]:
                    min_edge[v] = matrix[u][v]
    
    return total_weight
