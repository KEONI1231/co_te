from collections import deque

def bfs(start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")
        graph[current_node].sort()
        for i in graph[current_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(start, visited):
    visited[start] = True
    print(start, end = " ")
    graph[start].sort()
    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited)

total_node, total_edge, start_node = map(int, input().split())

"""
    graph의 0 인덱스는 버리니까 사이즈는 + 1.
    인덱스의 총 수는 노드의 수.
"""
graph = [[] for _ in range(total_node+1)]

for i in range(total_edge):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dfs_visited = [False] * (total_node + 1)
bfs_visited = [False] * (total_node + 1)

dfs(start_node, dfs_visited)
print()
bfs(start_node, bfs_visited)

