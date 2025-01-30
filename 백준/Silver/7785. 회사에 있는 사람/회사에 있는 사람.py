n = int(input())
dic = {}

for _ in range(n):
    name, state = input().split()
    if state == 'leave':
        del dic[name]
    else :
        dic[name] = state

for n in sorted(dic.keys(), reverse=True):
    print(n)