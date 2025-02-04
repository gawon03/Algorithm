from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

diff = 0
for card in combinations(cards, 3):
    if m-sum(card) >=0 :
        diff = max(diff, sum(card))
        
print(diff)
