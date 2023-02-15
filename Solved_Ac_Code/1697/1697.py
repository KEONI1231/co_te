from collections import deque
a,b = map(int, input().split())

cnt = 0
direction = [0,-1,1,2]
def bfs(x):
    global cnt
    que = deque()
    que.append(x)
    while que:
        node = que.popleft()
        print(node)
        for i in direction:
            if i != 2 :
                node += i
            else
                node = node * 2
            if(node != b) :
                que.append(node)
                cnt +=1
bfs(a)
print(cnt)