n, l = map(int, input().split())

map_ = [list(map(int, input().split())) for _ in range(n)]

def check(i, j):
    global num, grad_desc, grad_asc, stat, stop
#    print(i, j, num, cnt, stat)
    if abs(num - map_[i][j]) > 1:
        stat = False
        stop = True
        return
    else:
        # 숫자가 같으면 경사도 놓기
        if num == map_[i][j]:
            if grad_desc > 0:
                grad_desc -= 1
            else :
                grad_asc += 1
        else :
            # 경사도를 완전히 놓지 못하고 다시 경사가 발생할 경우 실패
            if grad_desc > 0:
                stat = False
                stop = True
                return
            else :
                # 경사가 하강할 경우
                if num > map_[i][j]:
                    grad_desc = l - 1
                    grad_asc = 0
                # 경사가 상승할 경우
                else :
                    if grad_asc < l:
                        stat = False
                        stop = True
                        return
                    grad_asc = 1
        num = map_[i][j]


answer = 0

for i in range(n):
    num = map_[i][0]
    grad_asc = 1
    grad_desc = 0
    stat = True
    stop = False
    for j in range(1, n):
        check(i, j)
        if stop == True:
            break
    if stat == True and grad_desc == 0 :
        answer += 1

for j in range(n):
    num = map_[0][j]
    grad_asc = 1
    grad_desc = 0
    stat = True
    stop = False
    for i in range(1, n):
        check(i, j)
        if stop == True :
            break
    if stat == True and grad_desc == 0 :
        answer += 1

print(answer)