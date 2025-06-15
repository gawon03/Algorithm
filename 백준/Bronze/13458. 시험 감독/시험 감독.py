n = int(input()) # 시험장 개수
a = list(map(int, input().split())) # i번 시험장에 있는 응시자의 수
b, c = map(int, input().split()) # 총감독관, 부감독관 각각의 감시 가능 응시자 수


def solution(n, a, b, c):
    answer = n
    for i in range(n):
        if a[i] > b:
            answer += (a[i] - b) // c
            if (a[i] - b) % c != 0:
                answer += 1
    print(answer)
    return
solution(n, a, b, c)