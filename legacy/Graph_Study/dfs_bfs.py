#dfs
#깊이 우선 탐색
#스택 자료구조, 재귀함수

# 6 ~ 25 dfs 기본형
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end =' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)

visited = [False]*9
dfs(graph, 1, visited)

#bfs 너비우선 탐색
#큐 자료구조 활용
#인접한 노드를 전부 한번에 큐에 삽입
#31 ~ 56 기본 bfs
from collections import deque

def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
print()
visited = [False] * 9
bfs(graph, 1, visited)

