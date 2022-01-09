n,m = map(int, input().split())
graph = []
for i in range(n):
  row = list(map(int, input()))
  graph.append(row)

cnt = 0

# 그래프의 마지막 여부 체크 (더이상 움직일 수 있는 칸 없음)
def chkGraphEnd(x,y):
  nx1, nx2, ny1, ny2 = 1

  if x>1:
    nx1 = graph[x-1]
  if x<n:
    nx2 = graph[x+1]
  if y>1:
    ny1 = graph[y-1]
  if y<m:
    ny2 = graph[y+1]
  
  if nx1*nx2*ny1*ny2 == 1:
    return True
  else:
    return False

  

def bfs(x,y):
  # 종료 조건
  if x<0 or y<0 or x>n-1 or y>m-1:
    return False
  if graph[x][y]==1:
    return False

 
  # 방문 점 1로 변경
  graph[x][y]=1
  # 재귀
  bfs(x-1, y)
  bfs(x, y-1)
  bfs(x+1, y)
  bfs(x, y+1)

  return True

result = 0
for i in range(n):
  for j in range(m):
    if bfs(i, j):
      result +=1

print(result)
