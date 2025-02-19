c = int(input())
n = int(input())

computers = [0]*(c+1)
network = [[] for _ in range(c+1)]

for _ in range(n):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
    
from collections import deque
queue = deque(network[1])

while queue:
    no = queue.popleft()
    computers[no] = 1
    for net in network[no]:
        if computers[net] == 0:
            queue.append(net)
computers[1] = 0
print(sum(computers))