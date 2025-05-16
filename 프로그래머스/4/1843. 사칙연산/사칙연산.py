# M[(i, j)]
# nums[i] 부터 nums[j]까지 연산했을 때 나올 수 있는 최댓값
# m[(i, j)]
# nums[i] 부터 nums[j]까지 연산했을 때 나올 수 있는 최솟값
M, m = {}, {}
# 점화식
# i~j를 두 부분으로 분할하는 모든 k에 대해서 (k=i+1, i+2, ..., j)
# --> i~k-1 / k~j로 나뉜다고 하자
# 나올 수 있는 연산의 최댓값, 최솟값을 저장해 두어야 한다.
# ops[k-1]의 경우에 따라 나뉜다
# ops[k-1] == '-'인 경우,
# 최댓값을 위해서는 M[(i, k-1)] - m[(k, j)] 를 기억해둔다.
# 최솟값을 위해서는 m[(i, k-1)] - M[(k, j)] 를 기억해둔다.
# ops[k-1] == '+'인 경우,
# 최댓값을 위해서는 M[(i, k-1)] + M[(k, j)] 를 기억해둔다.
# 최솟값을 위해서는 m[(i, k-1)] + m[(k, j)] 를 기억해둔다.

def solution(arr):
    nums = [int(x) for x in arr[::2]]
    ops = [x for x in arr[1::2]]
    
    for i in range(len(nums)):
        M[(i, i)] = nums[i]            # M[(a, b)] : nums[a]부터 nums[b]까지 괄호로 묶었을 때 가능한 최댓값
        m[(i, i)] = nums[i]
    
    for d in range(1, len(nums)):      # 구간 길이 d : 1부터 시작
        for i in range(len(nums)):     # 구간의 시작 인덱스
            j = i + d                  # 구간의 끝 인덱스
            if j >= len(nums):
                continue
            
            maxcandidates, mincandidates = [], []
            for k in range(i+1, j+1):  # 연산자 기준으로 나눌 위치 (구간을 나눠 연산을 수행하는 지점)
                if ops[k-1] == '-':
                    mx = M[(i, k-1)] - m[(k, j)]
                    mn = m[(i, k-1)] - M[(k, j)]
                    maxcandidates.append(mx)
                    mincandidates.append(mn)
                else:
                    mx = M[(i, k-1)] + M[(k, j)]
                    mn = m[(i, k-1)] + m[(k, j)]
                    maxcandidates.append(mx)
                    mincandidates.append(mn)
            
            M[(i, j)] = max(maxcandidates)
            m[(i, j)] = min(mincandidates)
                    
    return M[(0, len(nums) - 1)]