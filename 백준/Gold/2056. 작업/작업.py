n = int(input()) # 작업의 개수
dp = [0]*(n+1)   # dp[i] : i번째 작업을 끝냈을 때 걸리는 최대 시간

for i in range(1, n+1):
    work, count, *pre = map(int, input().split())
    # work  : i번째 작업 자체에 걸리는 시간
    # count : i번째 작업을 하기 위해 필요한 선수작업 개수
    # pre   : 선수작업들의 번호 리스트
    # *pre : 입력 받은 값 중 세 번째 이후 값들을 전부 리스트로 담기

    dp[i] = work   # 기본값 : 선수작업이 없다면 자기 작업 시간만큼 걸림
    for j in pre:  # 선수작업이 있을 경우
        dp[i] = max(dp[i], dp[j]+work)
        # i번 작업을 끝내려면 가장 늦게 끝나는 선수작업 j를 기다려야 시작할 수 있음
        # 따라서 'j번을 끝내는 데 걸린 시간 + i번 작업시간'과 비교해서 최댓값

print(max(dp)) # 모든 작업을 끝내는 데 필요한 최소 전체 시간 