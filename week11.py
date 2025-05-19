## DFS : 기피 우선 탐색
## 재귀함수 사용 및 방문한 것을 확인하는 것
graph = [
    [0, 1, 1, 0, 0, 0, 0, 0], # index 0
    [1, 0, 0, 1, 0, 0, 0, 0], # index 1
    [1, 0, 0, 1, 0, 0, 0, 0], # index 2
    [0, 1, 1, 0, 1, 1, 1, 0], # index 3
    [0, 0, 0, 1, 0, 1, 0, 0], # index 4
    [0, 0, 0, 1, 1, 0, 0, 0], # index 5
    [0, 0, 0, 1, 0, 0, 0, 1], # index 6
    [0, 0, 0, 0, 0, 0, 1, 0]  # index 7
]

def dfs(g, i, visited):
    visited[i] = True
    print(chr(ord('A')+i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

def bfs(g, i, visited):
    pass

visited_dfs = [False for _ in range(len(graph))]  ## 기본값 False
visited_bfs = [0 for _ in range(len(graph))]  ## 기본값 0
dfs(graph, 7, visited_dfs)
print()
dfs(graph, 2, visited_bfs) # 너비 우선 탐색