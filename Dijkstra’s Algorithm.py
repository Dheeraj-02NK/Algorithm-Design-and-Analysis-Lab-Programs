import heapq

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0

    min_heap = [(0, source)]  # (distance, vertex)

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)

        # Ignore outdated entries
        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(min_heap, (dist[v], v))

    return dist


# -------- MAIN PROGRAM --------
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

graph = [[] for _ in range(V)]

print("Enter edges in format: u v weight")
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))   # remove this line if graph is directed

source = int(input("Enter source vertex: "))

distances = dijkstra(graph, source)

print("\nShortest distances from source:")
for i in range(V):
    print(f"Vertex {i} -> {distances[i]}")
