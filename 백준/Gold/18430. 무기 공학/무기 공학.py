n, m = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(n)]

boomerang = [[(0, -1), (1, 0)], [(0, -1), (-1, 0)],
             [(-1, 0), (0, 1)], [(0, 1), (1, 0)]]
visited = [[False]*m for _ in range(n)]
ans = 0


def bt(x, y, total):
    global ans
    # 행열 진행 처리(한 행 끝나면 다음 행으로)
    if y >= m:
        x += 1
        y = 0
        if x >= n: # 다 돌면 최댓값 갱신 후 종료
            ans = max(ans, total)
            return

    # (x,y) 칸이 비었으면 부메랑 놓기 시도
    if not visited[x][y]:
        for a, b in boomerang:  # 4방향 부메랑 가능한지
            ax, ay = x+a[0], y+a[1]
            bx, by = x+b[0], y+b[1]
            # 두 팔의 좌표가 범위 내이고, 아직 미사용이면
            if 0 <= ax < n and 0 <= ay < m and 0 <= bx < n and 0 <= by < m and not visited[ax][ay] and not visited[bx][by]:
                # 3칸 사용 표시
                visited[ax][ay] = True
                visited[bx][by] = True
                visited[x][y] = True
                # 점수 더하고 다음 칸으로
                bt(x, y+1, total+woods[x][y] *
                    2+woods[ax][ay]+woods[bx][by])
                # 백트래킹(원상복구)
                visited[ax][ay] = False
                visited[bx][by] = False
                visited[x][y] = False
    bt(x, y+1, total)   # 이 자리에 안 놓음


bt(0, 0, 0)
print(ans)