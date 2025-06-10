count = 1
temp = True
op = []
stack = []

N = int(input())

for _ in range(N):
    num = int(input())
    
    # num 이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1
    
    # 스택 맨 뒤 숫자와 num이랑 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

# 스택 수열을 만들 수 있는지 여부에 따라 출력
if temp :
    for i in op:
        print(i)
else :
    print('NO')