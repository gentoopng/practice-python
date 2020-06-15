# THIS IS A WRONG ANSWER
N = int(input())
A = list(map(int, input().split()))

foundList = []
for i in range(0, N - 1, 1):
    for j in range(0, N - 1, 1):
        if i != j:
            if A[i] % A[j] != 0:
                if foundList == None or not i in foundList:
                    foundList.append(i)
print(len(foundList))