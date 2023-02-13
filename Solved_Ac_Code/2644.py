#촌수 계산
from collections import deque

n = int(input()) #사람수
a,b = map(int,input().split()) #계산해야 할 촌수
m = int(input()) #관계의 수
graph = [[] * n for _ in range(n+1)]
visit = [False] * (n+1)
result = [False] * (n+1)

for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a):
    que = deque()
    que.append(a)
    visit[a] = True
    while que:
        node = que.popleft()
        for i in graph[node]:
            if(visit[i] == False):
                que.append(i)
                visit[i] = True
                result[i] = result[node] + 1

bfs(a)
if(result[b] != 0):
    print(result[b])
else :
    print(-1)