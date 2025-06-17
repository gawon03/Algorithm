n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
max_ = 0
def shape1(x, y):
  global max_
  if 0 <= x + 3 < n:
    temp = paper[x][y] + paper[x+1][y] + paper[x+2][y] + paper[x+3][y]
    max_ = max(max_, temp)
  if 0 <= y + 3 < m:
    temp = paper[x][y] + paper[x][y+1] + paper[x][y+2] + paper[x][y+3]
    max_ = max(max_, temp)
  return max_

def shape2(x, y):
  global max_
  if 0<=x+1<n and 0<=y+1<m:
    temp = paper[x][y] + paper[x+1][y] + paper[x+1][y+1] + paper[x][y+1]
    max_ = max(max_, temp)
  return max_

def shape3(x, y):
  global max_
  if 0<=x+2<n and 0<=y+1<m:
    temp1 = paper[x][y]+paper[x+1][y]+paper[x+2][y]+paper[x+2][y+1]
    temp2 = paper[x][y]+paper[x][y+1]+paper[x+1][y+1]+paper[x+2][y+1]
    max_ = max(max_, temp1, temp2)
  if 0<=x-2<n and 0<=y+1<m:
    temp1 = paper[x][y]+paper[x-1][y]+paper[x-2][y]+paper[x-2][y+1]
    temp2 = paper[x][y]+paper[x][y+1]+paper[x-1][y+1]+paper[x-2][y+1]
    max_ = max(max_, temp1, temp2)
  if 0<=x+1<n and 0<=y+2<m:
    temp1 = paper[x][y]+paper[x][y+1]+paper[x][y+2]+paper[x+1][y+2]
    temp2 = paper[x][y]+paper[x+1][y]+paper[x+1][y+1]+paper[x+1][y+2]    
    max_ = max(max_, temp1, temp2)
  if 0<=x-1<n and 0<=y+2<m:
    temp1 = paper[x][y]+paper[x][y+1]+paper[x][y+2]+paper[x-1][y+2]
    temp2 = paper[x][y]+paper[x-1][y]+paper[x-1][y+1]+paper[x-1][y+2]    
    max_ = max(max_, temp1, temp2)
  return max_

def shape4(x, y):
  global max_
  if 0<=x+2<n and 0<=y+1<m:                                               # |
    temp = paper[x][y]+paper[x+1][y]+paper[x+1][y+1]+paper[x+2][y+1]      #  ㅡ
    max_ = max(max_, temp)                                                #    |

  if 0<=x-2<n and 0<=y+1<m:                                               #    |
    temp = paper[x][y]+paper[x-1][y]+paper[x-1][y+1]+paper[x-2][y+1]      #  ㅡ
    max_ = max(max_, temp)                                                # |

  if 0<=x+1<n and 0<=y+2<m:                                               # ㅡ
    temp = paper[x][y]+paper[x][y+1]+paper[x+1][y+1]+paper[x+1][y+2]      #   |
    max_ = max(max_, temp)                                                #    --

  if 0<=x-1<n and 0<=y+2<m:                                               #    ㅡ
    temp = paper[x][y]+paper[x][y+1]+paper[x-1][y+1]+paper[x-1][y+2]      #   |
    max_ = max(max_, temp)                                                # ㅡ

  return max_

def shape5(x, y):
  global max_
  if 0<=x+1<n and 0<=y+2<m: # ㅜ 
    temp = paper[x][y]+paper[x][y+1]+paper[x][y+2]+paper[x+1][y+1]
    max_ = max(max_, temp)
  if 0<=x-1<n and 0<=y+2<m: # ㅗ
    temp = paper[x][y]+paper[x][y+1]+paper[x][y+2]+paper[x-1][y+1]
    max_ = max(max_, temp)
  if 0<=x+2<n and 0<=y-1<m: # ㅓ
    temp = paper[x][y]+paper[x+1][y]+paper[x+2][y]+paper[x+1][y-1]
    max_ = max(max_, temp)
  if 0<=x+2<n and 0<=y+1<m: # ㅏ
    temp = paper[x][y]+paper[x+1][y]+paper[x+2][y]+paper[x+1][y+1]
    max_ = max(max_, temp)
  return max_

def solution():
  for i in range(n):
    for j in range(m):
      max_ = shape1(i, j)
      max_ = shape2(i, j)
      max_ = shape3(i, j)
      max_ = shape4(i, j)
      max_ = shape5(i, j)
  return print(max_)

solution()