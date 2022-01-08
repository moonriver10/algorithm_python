n = int(input())
move = input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

x,y = 1,1
for i in range(len(move)):
  for j in range(len(move_types)):
    if(move_types[j]==move[i]):
      
      nx = x + dx[j]
      ny = y + dy[j]
      
      if nx<1 or ny <1 or nx > n or ny > n :
        continue
      # 이동 수행
      x = nx
      y = ny

print(x,y)
