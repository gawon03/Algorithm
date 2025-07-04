from collections import deque

# 행(r), 열(c), 시간(t)
r, c, t = map(int, input().split())

# 공기청정기(-1), 나머지는 미세먼지 양
# 공기청정기는 위아래로 두 칸이상 떨어져있음
room = [list(map(int, input().split())) for _ in range(r)]


# 공기청정기 위치 저장
air_ = []
for x in range(r):
    if room[x][0] == -1:
        air_.append(x)
        
# 확산 방향   
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 확산 방향
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def Dust():
    room_new = [[0]*c for _ in range(r)]
    room_new[air_[0]][0] = -1
    room_new[air_[1]][0] = -1

    for x in range(r):
        for y in range(c):
            # 미세먼지가 있으면 확산시킨다
            if room[x][y] > 0 :

                room_new[x][y] += room[x][y]
                temp = room[x][y] // 5

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0<= nx < r and 0 <= ny < c :
                        if room[nx][ny] != -1:
                            room_new[nx][ny] += temp
                            room_new[x][y] -= temp
    return room_new


def Air(r1, r2, dx_, dy_):
    global room
    i = 0
    if r1 in [0, r]:
        air_x = r2-2
    else :
        air_x = r1+1

    queue = deque()
    queue.append((air_x,0))

    while i<4:
        x, y = queue.popleft()
        nx = x + dx_[i]
        ny = y + dy_[i]

        if r1 <= nx < r2 and 0 <= ny < c:
            if room[nx][ny] != -1:
                #print(x, y, nx, ny)
                room[x][y] = room[nx][ny]
                queue.append((nx, ny))
            else :
                room[x][y] = 0
                break
        else:
            i += 1
            queue.append((x, y))
    return
    
for _ in range(t):
    room = Dust()
    Air(0, air_[0]+1, [-1, 0, 1, 0], [0, 1, 0, -1])
    Air(air_[1], r, [1, 0, -1, 0], [0, 1, 0, -1])


answer = 0
for x in range(r):
    for y in range(c):
        if room[x][y] > 0:
            answer += room[x][y]

print(answer)