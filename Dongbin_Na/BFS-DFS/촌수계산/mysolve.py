from collections import deque


def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        node = queue.popleft()
        for index in graph[node]:
            if not visited[index]:
                visited[index] = True
                queue.append(index)
                distance_list[index] = distance_list[node] + 1
                print(node, distance_list[index])

people = int(input())
visited = [False] * (people + 1)
distance_list = [0] * (people + 1)

p1, p2 = map(int, input().split())
edge = int(input())
graph = [[] for _ in range(people + 1)]
for i in range(edge):
    x1, x2 = map(int, input().split())
    graph[x1].append(x2)
    graph[x2].append(x1)

bfs(p1)

if distance_list[p2] != 0:
    print(distance_list[p2])
else:
    print(-1)
