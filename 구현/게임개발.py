n,m = map(int, input().split())
x,y,direction = map(int, input().split())

map_arr =[]
for i in range(n):
  row = list(map(int, input().split()))
  map_arr.append(row)


visited = [[0]*m for i in range(n)] # 방문여부

#북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


#왼쪽으로 회전
def turn_left():
  global direction #전역변수로 사용
  direction -= 1
  if direction == -1:
    direction = 3
    
count = 0

#시뮬레이션
while True:
  turn_left() 

  nx = x + dx[direction]
  ny = y + dy[direction]

  if map_arr[nx][ny] == 0 and visited[nx][ny] == 0: # 갈 수 있으면 이동
    x = nx
    y = ny
    count += 1
    turn_time = 0 # 다시 turn_time 초기화
    continue
  else:
    turn_time += 1

  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x-dx[direction]
    ny = y-dy[direction]

    if map_arr[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_time=0
