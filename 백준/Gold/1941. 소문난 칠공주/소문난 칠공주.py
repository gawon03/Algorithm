from collections import deque


# bfs로 7명의 여학생이 붙어있는지 확인한다.
def dfs_2(visited, r, c):
    global check
    global count_temp

    if r < 0 or r >= 5 or c < 0 or c >= 5:
        return

    if visited[r][c] == 0:  # 만약 여학생 위치라면
        visited[r][c] = 1  # 그 값을 1로 변경한 후
        count_temp += 1  # 붙어있는 학생수 +1
    else:
        return

    if count_temp == 7:  # 만약 7명이 붙어있다면
        check = True  # check 변경
        return

    dr = [-1, +1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, +1]  # 상하좌우

    for i in range(4):
        dfs_2(visited, r + dr[i], c + dc[i])


def dfs(depth, start, count):
    global result
    global check
    global count_temp

    if count >= 4:  # 만약 임도연파가 4명이상이라면
        return  # 재귀 탈출

    if depth == 7:  # 7명을 뽑았다면
        # 7명 여학생 위치 방문처리를 위한 리스트 1로 처리
        visited = [[1] * 5 for _ in range(5)]
        for i in arr:  # 여학생 위치 0으로 초기화
            visited[i[0]][i[1]] = 0

        dfs_2(visited, arr[0][0], arr[0][1])  # 여학생들이 붙어있는지 체킹
        if check:
            result += 1  # 횟수 1번 추가
            check = False
        count_temp = 0
        return

    for i in range(start, 25):
        r = i // 5  # 총 25번 중 행은 i 나누기 5와 같다.
        c = i % 5  # 총 25번 중 열은 i를 5로 나눈 나머지와 같다.
        arr.append((r, c))  # 해당 위치를 추가
        dfs(depth + 1, i + 1, count + (students[r][c] == 'Y'))  # 재귀 돈다.
        arr.pop()  # 해당 위치를 제거


students = [list(input()) for _ in range(5)]
arr = []
result = 0
check = False  # 7명이 붙어있는지 여부
count_temp = 0  # 몇명이 붙어있는지 확인
dfs(0, 0, 0)
print(result)