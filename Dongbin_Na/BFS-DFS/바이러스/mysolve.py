from collections import deque
def bfs(start, visited):
    global cnt
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        current_node = queue.popleft()
        for i in graph[current_node]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = True

cnt = 0
computer_cnt = int(input())
network_cnt = int(input())
graph = [[] for _ in range(computer_cnt+1)]
for i in range(network_cnt):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

visited = [False] * (computer_cnt + 1)
bfs(1, visited)
print(cnt)
