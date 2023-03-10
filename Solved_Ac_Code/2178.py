# 그래프 미로찾기

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        print('pop(' + str(x) + ',' + str(y)+')')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                print(str(nx) + " : " +str(ny))
                que.append((nx,ny))
                print(que)

    return graph[n-1][m-1]

print(bfs(0, 0))
