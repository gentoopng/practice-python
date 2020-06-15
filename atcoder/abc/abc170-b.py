X, Y = map(int, input().split())
ans = "No"

for a in range(100):
    for b in range(100):
        x = a + b
        y = 2 * a + 4 * b
        if x == X and y == Y:
            ans = "Yes"

print(ans)