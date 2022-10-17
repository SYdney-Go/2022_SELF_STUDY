def dijkstra(edges, num_v):
    dist = [float("inf") * num_v]
    dist[0] = 0
    q = [i for i in range(num_v)]
    
    while len(q) > 0:
        