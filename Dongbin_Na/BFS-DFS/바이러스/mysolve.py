from collections import deque
cnt = 0
def bfs(start, visited) :
    global cnt
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        current_node = queue.popleft()
        for i in graph[current_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
computer_cnt = int(input())
network_cnt = int(input())
graph = [[] for i in range( computer_cnt +1)]
for i in range(network_cnt):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)
visited = [False] * (computer_cnt + 1)
bfs(1, visited)
print(cnt)