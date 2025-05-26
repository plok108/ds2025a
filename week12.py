from collections import deque  # deque 입출입 양방향으로 처리됨

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0], # index 0 A
    [1, 0, 0, 1, 0, 0, 0, 0], # index 1 B
    [1, 0, 0, 1, 0, 0, 0, 0], # index 2 C
    [0, 1, 1, 0, 1, 1, 1, 0], # index 3 D
    [0, 0, 0, 1, 0, 1, 0, 0], # index 4 E
    [0, 0, 0, 1, 1, 0, 0, 0], # index 5 F
    [0, 0, 0, 1, 0, 0, 0, 1], # index 6 G
    [0, 0, 0, 0, 0, 0, 1, 0]  # index 7 H
]

def dfs(g, i, visited):
    visited[i] = True
    print(chr(ord('A')+i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

def bfs(g, i, visited):
    queue = deque([i])
    visited[i] = 1
    # while len(queue) != 0:
    while queue:
        i = queue.popleft()
        print(chr(ord('A') + i), end=' ')
        for j in range(len(graph)):
            if g[i][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j] += 1

visited_dfs = [False for _ in range(len(graph))]  ## 기본값 False
visited_bfs = [0 for _ in range(len(graph))]  ## 기본값 0
dfs(graph, 7, visited_dfs)
print()
dfs(graph, 4, visited_bfs) # 너비 우선 탐색