def solution(name):
    N = len(name)
    spell_move = sum(map(lambda x : min(ord(x)-ord('A'), ord('Z')-ord(x)+1), name))
    cursor_move = len(name) - 1

    for i, spell in enumerate(name):
        # 해당 알파벳 이후부터 연속된 A 문자열 찾기
        idx = i + 1
        while idx < len(name) and name[idx] == 'A':
            idx += 1
        
        # 아래 3가지 경우 중 최소 이동 값으로 갱신
        # 1. 이전 커서 이동 값(초기값 - 이름의 길이 - 1)
        # 2. 연속된 A의 왼쪽 시작
        # 3. 연속된 A의 오른쪽 시작
        cursor_move = min([cursor_move, 2*i+N-idx, i+2*(N-idx)])
        
    return spell_move + cursor_move