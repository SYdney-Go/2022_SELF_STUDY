# 최단 경로 탐색 문제 찾기
def bellman_ford(edges, num_v):
    # 모든 노드의 값을 무한대로 초기화
    dist = [float('inf') for i in range(num_v)]
    # 첫번째 노드의 값을 0으로 설정
    dist[0] = 0
    
    changed = True
    while changed:
        changed = False
        for edge in edges:
            # edge[0] = 시작 노드, edge[1] = 도착 노드, edge[2] = 값
            # 도착노드 > 시작 노드 + 값 -> 시작노드는 끝 노드 + 값으로 갱신
            # 즉 기존의 비용보다 더 작은 값이 있는 경우 갱신하기
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                changed = True
    return dist

# edges = 시작점, 도착점, 점수
edges = [
    [0,1,4], [0,2,3], [1,2,1], [1,3,1],
    [1,4,5], [2,5,2], [4,6,2], [5,4,1],
    [5,6,4]
]

print(bellman_ford(edges, 7))