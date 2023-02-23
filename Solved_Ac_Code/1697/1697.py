from collections import deque

a,b = map(int, input().split())
max = 10**5
result = [0] * (max)

def bfs():
    que = deque()
    que.append(a)

