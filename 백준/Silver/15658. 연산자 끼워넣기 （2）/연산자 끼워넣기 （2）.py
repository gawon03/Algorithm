N = int(input())
array = list(map(int, input().split()))
operator = list(map(int, input().split())) # +, -, x, %

def caculate(i, temp, cnt):
    num = temp
    if i == 0:
        num += array[cnt]
    elif i == 1:
        num -= array[cnt]
    elif i == 2:
        num *= array[cnt]
    else :
        if num * array[cnt] < 0:
            num = abs(num) // abs(array[cnt]) * -1
        else:
            num //= array[cnt]
    return num


def dfs(temp, cnt):
    global mx, mn
    
    # 종료 조건
    if cnt == N-1:
        mx = max(temp, mx)
        mn = min(temp, mn)
        return mx, mn

    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1
            dfs(caculate(i, temp, cnt+1), cnt+1)
            operator[i] += 1

mx, mn = -1e9, 1e9
dfs(array[0], 0)

print(mx)
print(mn)