from collections import deque

F, S, G, U, D = map(int, input().split())


def bfs(f, s, g, u, d):
  queue = deque()
  queue.append(s)
  visited[s] = 1
  while queue:
    node = queue.popleft()
    if node == g:
      return visited[node]-1
    else:
      for x in (node + u, node - d):
        if (0 < x <= f) and visited[x] == 0:
          visited[x] = visited[node] + 1
          queue.append(x)

  return "use the stairs"


visited = [0] * (F + 1)

print(bfs(F, S, G, U, D))

#10 1 10 2 1

#100 2 1 1 0
