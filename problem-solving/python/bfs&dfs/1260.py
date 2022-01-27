from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 인접 행렬 생성, [[],[],[],.....,[]]

for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)  # 무방향 그래프
    graph[n2].append(n1)

graph = [sorted(i) for i in graph]

visited = [False] * (N + 1)  # flag init


def dfs(graph, v, visited):  # dfs function
    visited[v] = True
    print(v, end=' ')
    for n in graph[v]:
        if not visited[n]:
            dfs(graph, n, visited)


def bfs(graph, v):
    visited = [False] * (N + 1)  # flag init
    queue = deque([v])  # contains v in queue (양방향 큐 생성)
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for n in graph[v]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True


dfs(graph, V, visited)
print()
bfs(graph, V)
