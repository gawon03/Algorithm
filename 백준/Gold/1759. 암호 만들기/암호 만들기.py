# 서로다른 L개의 소문자
# 모음 최소 1개, 자음 죄소 2개 구성
# 증가하는 순서로 배열

L, C = map(int, input().split())
alpha = list(input().split())
alpha.sort()
aeiou = ['a', 'e', 'i', 'o', 'u']

def dfs(idx):

    # 종료 조건
    if len(ans) == L and 2 <= sum(map(lambda x : 0 if x in 'aeiou' else 1, ans)) <= L-1:
        print(''.join(ans))
        return

    for i in range(idx, C):
        ans.append(alpha[i])
        dfs(i+1)
        ans.pop()

ans = []
dfs(0)