def solution(brown, yellow):
    div = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            x = yellow/i
            y = i
            div.append([x,y])
            if 2*(x+y)+4 == brown:
                return [x+2, y+2]