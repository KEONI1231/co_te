from collections import deque


def bfs(i, j, height):
  queue = deque()
  queue.append([i, j])
  copy_graph[i][j] = 0
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      now_x = x + dx[i]
      now_y = y + dy[i]
      if now_x < 0 or now_y < 0 or now_x >= N or now_y >= N:
        continue
      if copy_graph[now_x][now_y] > height:
        continue
      if copy_graph[now_x][now_y] <= height and copy_graph[now_x][now_y] != 0:
        queue.append([now_x, now_y])
        copy_graph[now_x][now_y] = 0


def bfs1(i, j):
  queue1 = deque()
  queue1.append([i, j])
  copy_graph[i][j] = -1
  while queue1:
    x, y = queue1.popleft()
    for i in range(4):
      now_x = x + dx[i]
      now_y = y + dy[i]
      if now_x < 0 or now_y < 0 or now_x >= N or now_y >= N:
        continue
      if copy_graph[now_x][now_y] == 0:
        continue
      if copy_graph[now_x][now_y] != 0 and copy_graph[now_x][now_y] != -1:
        queue1.append([now_x, now_y])
        copy_graph[now_x][now_y] = -1


graph = []

height_list = []
N = int(input())
copy_graph = [[0] * N for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
  graph.append(list(map(int, input().split())))

for i in range(N):
  for j in range(N):
    if graph[i][j] not in height_list:
      height_list.append(graph[i][j])
    copy_graph[i][j] = graph[i][j]
height_list.sort()

cnt = 0
cnt_list = []
for k in height_list:
  for i in range(N):
    for j in range(N):
      if copy_graph[i][j] <= k and copy_graph[i][j] != 0:
        bfs(i, j, k)
  for i in range(N):
    for j in range(N):
      if copy_graph[i][j] != 0 and copy_graph[i][j] != -1:
        bfs1(i, j)
        cnt += 1

  cnt_list.append(cnt)
  cnt = 0
  for m in range(N):
    for n in range(N):
      copy_graph[m][n] = graph[m][n]

cnt_list.sort(reverse=True)


if (cnt_list[0] == 0):
  print(1)
else:
  print(cnt_list[0])
"""

"""
