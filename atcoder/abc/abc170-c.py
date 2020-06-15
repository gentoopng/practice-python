X, N = map(int, input().split())
ps = list(map(int, input().split()))
ps.sort()

diff = 1000
ans = None
for i in range(X - 51, X + 51, 1):
    isInPs = False
    index = 0
    for j in ps:
        if ps[index] == i:
            isInPs = True
            break
        index += 1
    if isInPs == False:
        testDiff = abs(X - i)
        if testDiff < diff:
            diff = testDiff
            ans = i
print(ans)