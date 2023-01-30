"""
    바이러스 문제
n = int(input()) #컴퓨터 수.
m = int(input()) #컴퓨터 쌍의 수.
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
print(graph)
visited = [0]*(n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
dfs(1)
print(cnt)
"""

#bfs
from collections import deque
n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
node = 0
visited = [False] * (n+1)
def bfs(start):
    que = deque([start])
    visited[start] = True
    global cnt
    while que:
        v = que.popleft()
        for i in graph[v]:
            if(visited[i] == False):
                que.append(i)
                visited[i] = True
                cnt+=1
                
    
        

bfs(1)
print(cnt)