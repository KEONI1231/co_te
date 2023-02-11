# 다시풀기


from collections import deque

n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[] * n for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
result = [0 for _ in range(n + 1)]
cnt = 0;


def bfs(x):
    global cnt
    que = deque()
    que.append(x)
    visited[x] = True

    while que:
        a1 = que.popleft()
        for i in graph[a1]:
            if (visited[i] == False):
                que.append(i)
                visited[i] = True
                result[i] = result[a1] + 1


bfs(x)

if (result[y] != 0):
    print(result[y])

else:
    print("-1")
