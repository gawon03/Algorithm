def solution(sizes):
    a = 0
    b = 0
    for x, y in sizes:
        if x>y:
            a = max(a, x)
            b = max(b, y)
        else:
            a = max(a, y)
            b = max(b, x)
    return a*b