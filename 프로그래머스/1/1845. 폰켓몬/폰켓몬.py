# 선택 개수 : len(nums)/2
# nums의 nunique 값 확인하여
# nunique이 더 크면 선택개수, 선택개수가 더 크면 nunique값
# 리턴 값 : 최대 종류의 개수

def solution(nums):
    return min(len(nums)//2, len(set(nums)))