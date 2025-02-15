def solution(N, number):
    if N == number:
        return 1
    
    answer = -1
    # arr[i] : 주어진 수 N을 i+1번 사용해서 만들 수 있는 수들의 집합
    arr = [set() for _ in range(8)] # N 사용횟수가 8보다 크면 -1을 return하기 때문에 8개까지만 생성
    
    for i in range(len(arr)):
        arr[i].add(int(str(N)*(i+1)))
    
    # arr[i] 즉 N을 i+1개 사용했을 때 만들 수 있는 숫자 구하기
    for i in range(1,8):
        for j in range(i):
            for op1 in arr[j]: # op1 : 피연산자1, N을 j+1번 사용하여 만들 수 있는 숫자들
                for op2 in arr[i-j-1]: # op2 : 피연산자2, N을 i-j번 사용하여 만들 수 있는 숫자들
                    # op1과 op2를 사칙연산 --> 즉, N을 i+1번 사용하여 만들 수 있는 숫자를 구하게 되고 이를 arr[i]에 대입
                    arr[i].add(op1+op2)
                    arr[i].add(op1-op2)
                    arr[i].add(op1*op2)
                    if op2 != 0:
                        arr[i].add(op1//op2)
        if number in arr[i]: # N을 i+1번 사용했을 때 찾고자하는 값 number가 존재한다면 i+1 return
            answer = i+1
            break
    
    return answer