# 2667
# 단지 번호 붙이기
from collections import deque

a = int(input())

graph = []
for i in range(a):
    graph.append(list(map(int, input())))

cnt = 0
count = []
total_cnt = 0;
dx = [-1,1,0,0,0]
dy = [0,0,-1,1,0]

def bfs(x,y):
    global cnt
    que = deque()
    que.append([x,y])
    while que:
        x, y = que.popleft()

        for i in range(5):

            nx = x + dx[i]
            ny = y + dy[i]
            if(nx < 0 or nx >= a or ny < 0 or ny >= a):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                que.append([nx, ny])
                count[cnt-1]+=1;

for i in range(a):
    for j in range(a):
        if graph[i][j] == 1:
            count.append(cnt)
            total_cnt += 1
            bfs(i,j)


count.sort()
print(total_cnt)
for i in range(len(count)):
    print(count[i])
