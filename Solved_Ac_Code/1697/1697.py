from collections import deque
a,b = map(int, input().split())

cnt = 0
direction = [0,-1,1,2]

def bfs(x):
    global cnt
    que = deque()
    que.append(x)
    while que:
       pass
bfs(a)
print(cnt)