# 미로 찾기는 bfs!
from collections import deque

def bfs(x, y):
    queue = deque()


direction_x = [-1, 1, 0, 0]
direction_y = [0, 0, 1, 1]

graph = []

n, m = map(int, input().split())
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
bfs(0,0)