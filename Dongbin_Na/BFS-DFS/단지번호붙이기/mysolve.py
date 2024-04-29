from collections import deque


def bfs(i, j):
  global town_cnt
  #print(i, j, graph[i][j])
  queue = deque()
  queue.append([i, j])
  graph[i][j] = town_cnt
  home_cnt = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      new_x = x + dx[i]
      new_y = y + dy[i]
      if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
        continue
      if graph[new_x][new_y] == 0:
        continue
      if graph[new_x][new_y] == 1:
        queue.append([new_x, new_y])
        graph[new_x][new_y] = town_cnt
        home_cnt += 1
  town_cnt += 1
  print_list.append(home_cnt)


N = int(input())
graph = []
town_cnt = 2

for i in range(N):
  graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
print_list = []

for i in range(N):
  for j in range(N):
    if (graph[i][j] == 1):
      bfs(i, j)

print_list.sort()
print(town_cnt - 2)
for i in print_list:
  print(i)
