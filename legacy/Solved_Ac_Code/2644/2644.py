#촌수계산
from collections import deque
n = int(input()) #전체 사람수
a,b= map(int, input().split()) #구해야하는 관계
m = int(input()) #관계의 수

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a):
    que = deque()
    que.append(a)
    visited[a]= True
    while que:
        node = que.popleft()
        for i in graph[node]:
            if visited[i] != True:
                que.append(i)
                visited[i]=True
                result[i]= result[node] + 1
bfs(a)
if(result[b] != 0 ) :
    print(result[b])
else:
    print(-1)