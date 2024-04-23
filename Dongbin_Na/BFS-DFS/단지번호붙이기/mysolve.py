from collections import deque

def bfs(x, y):
    print(town_cnt)
    pass

graph = []
size = int(input())
town_cnt = 1

for i in range(size):
    graph.append(list(map(int, input())))

print(graph)

for i in range(size):
    for j in range(size):
        if(graph[i][j] == 1):
            bfs(i, j)