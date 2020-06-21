N, K = map(int, input().split())
prices = list(map(int, input().split()))

prices.sort()
result = 0

for i in range(K):
    result += prices[i]

print(result)