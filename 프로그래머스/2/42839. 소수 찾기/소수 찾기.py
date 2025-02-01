from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    lst = []
    # 숫자 조합 생성
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers,i):
            a = ''.join(num)
            lst.append(int(a))
    # 소수 개수 세기
    answer = 0
    for i in set(lst):
        if isPrime(i):
            answer += 1
    return answer