a, p = map(int, input().split())

array = [a]
while True:
    num = sum(int(i)**p for i in str(a))
    if num in set(array):
        print(array.index(num))
        break
    array.append(num)
    a = num