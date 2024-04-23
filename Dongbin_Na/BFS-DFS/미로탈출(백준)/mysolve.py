from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
#    print(n, m)
    # 큐가 빌 때까지 반복하기
    while queue:

        x, y = queue.popleft()
        for i in range(4):
            current_x = x + dx[i]
            current_y = y + dy[i]
            if current_x < 0 or current_x >= n or current_y < 0 or current_y >= m:
                #print('컨티뉴,',current_x,current_y,n,m)
                continue
            if graph[current_x][current_y] == 0:
                continue
            if graph[current_x][current_y] == 1:
                #print('정상', current_x, current_y)
                queue.append([current_x, current_y])
                graph[current_x][current_y] = graph[x][y] + 1
    return graph[n - 1][m - 1]


graph = []
n, m = map(int, input().split())
for i in range(n):
    graph.append(list(map(int, input())))

#print(n, m)
#print(graph)

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
print(bfs(0, 0))

