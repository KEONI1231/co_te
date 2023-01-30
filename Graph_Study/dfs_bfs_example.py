"""
    음료수 얼려먹기 문제
    n * m 개의 얼음 틀,
    구멍이 뚫린 부분은 0, 칸막이가 있는 부분은 1
    구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 부터있음
    총 생성되는 아이스크림
"""

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1

print(result)
