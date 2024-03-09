from collections import deque

n,m,start = map(int,input().split())
graph = [[] * n for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)
def dfs(start):

    dfs_visited[start] = True
    print(start, end = ' ')
    for i in graph[start]:
        if(dfs_visited[i] == False):
       
            dfs(i)

def bfs(start):
    
    que = deque([start])
    bfs_visited[start] = True
    while que:
        v=que.popleft()
        print(v, end=' ')
       
        for i in graph[v]:
            if(bfs_visited[i] ==False):
                
                bfs_visited[i] = True
                que.append(i)

dfs(start)
print()
bfs(start)
