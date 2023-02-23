
from collections import deque

a,b = map(int, input().split())
max = 10 ** 5
result = [0] * (max + 1)


def bfs():
    que = deque()
    que.append(a)
    while que:
        node = que.popleft()
        if node == b:
            print(result[node])
            break
        for i in (node -1, node+1, node *2):
            if 0 <= i <= max and not result[i]:
                result[i] = result[node] + 1
                que.append(i)

bfs()

