coins = list(map(int, input().split()))

coin_set = set()

for i in coins:
    if i not in coin_set:
        coin_set.add(i)
    else:
        dup = i
if len(coin_set) == 3:
    answer = max(coins) * 100
elif len(coin_set) == 2:
    answer = dup*100 + 1000
else:
    answer = 10000 + dup*1000
print(answer)
