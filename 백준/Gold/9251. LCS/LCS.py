# https://myjamong.tistory.com/317

word1 = input()
word2 = input()

l1, l2 = len(word1), len(word2)
dp = [0]*l2

# word1을 기준으로
for i in range(l1):
    mx = 0
    # word2 비교
    for j in range(l2):
        # dp[j]는 현재 word2[j]까지 고려한 LCS길이로
        # mx = dp[:j+1]까지의 최댓값으로 업데이트
        if mx < dp[j]:
            mx = dp[j]
        # 만약 문자가 같다면 이전 최적값(mx)에 1 더하기
        elif word1[i] == word2[j]:
            dp[j] = mx + 1
            
print(max(dp))