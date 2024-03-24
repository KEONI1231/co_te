num = int(input())
command = input().split()

initPoint_X, initPoint_Y = 1,1

# L, R, U, D에 따른 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

for plan in command:
    for i in range(len(move_types)):
        if(plan == move_types[i]) :
            nx = initPoint_X + dx[i]
            ny = initPoint_Y + dy[i]
    if nx < 1 or ny < 1 or nx > num or ny > num:
        continue

    initPoint_X = nx
    initPoint_Y = ny

print(initPoint_X, initPoint_Y)

