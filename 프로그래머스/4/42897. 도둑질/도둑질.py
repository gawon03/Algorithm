def solution(money):
    temp = [[0, 0], [0, 0]]
    for i in range(len(money)):
        if i == 0:
            new1 = max(temp[0][1], temp[0][0]+money[i])
            temp[0][0] = temp[0][1]
            temp[0][1] = new1
        if i > 0 and i < len(money)-1:
            new1 = max(temp[0][1], temp[0][0]+money[i])
            temp[0][0] = temp[0][1]
            temp[0][1] = new1
            
            new2 = max(temp[1][1], temp[1][0]+money[i])
            temp[1][0] = temp[1][1]
            temp[1][1] = new2
        if i == len(money)-1:
            new2 = max(temp[1][1], temp[1][0]+money[i])
            temp[1][0] = temp[1][1]
            temp[1][1] = new2
    return max(temp[0][1], temp[1][1])