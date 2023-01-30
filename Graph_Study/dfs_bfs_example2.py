
'''
    n * m 직사각형 미로
    현재 위치 (1,1), 출구는 (n,m)에 위치, 
    가면 안되는곳은 0, 갈 수 있는 곳은 1

    움직여야하는 최소칸
'''

from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx>= n or ny < 0 or ny >= m:
                print(str(nx) + " : " + str(ny) + ": case1" + " : " + str(graph[nx][ny]))
                continue
            if graph[nx][ny] == 0:
                print(str(nx) + " : " + str(ny) + ": case2"+ " : " + str(graph[nx][ny]))
                continue
            if graph[nx][ny] == 1:
                print(str(nx) + " : " + str(ny) + ": case3"+ " : " + str(graph[nx][ny]))
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]



n, m = map(int, input().split())

graph = [];
for i in range(n):
    graph.append(list(map(int, input())))

#이동할 수 있는 네가지 방향
#좌, 우, 하, 상
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))
