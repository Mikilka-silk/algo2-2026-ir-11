import heapq
import sys


def dijkstra(graph, start_node, n):
    distances = [float("inf")] * (n + 1)
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        if current_distance > distances[u]:
            continue

        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(priority_queue, (distance, v))
    return distances


def find_min_max_latency(n, clients, graph):
    clients_set = set(clients)
    min_max_latency = float("inf")

    for node in range(1, n + 1):
        if node in clients_set:
            continue

        distances = dijkstra(graph, node, n)

        current_max = 0
        for client in clients:
            latency = distances[client]
            if latency > current_max:
                current_max = latency

        if current_max < min_max_latency:
            min_max_latency = current_max

    return min_max_latency


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    idx += 2

    clients = []
    line_idx = 0
    lines = sys.stdin.readlines()
    if not lines: return
    
    n, m = map(int, lines[0].split())
    clients = list(map(int, lines[1].split()))
    
    graph = [[] for _ in range(n + 1)]
    for i in range(2, 2 + m):
        u, v, w = map(int, lines[i].split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    
