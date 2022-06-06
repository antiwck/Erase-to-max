def getResult (arr):
    min = 10**9+7
    dict = {}
    for i in arr:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for item in dict:
        if min > item*dict[item]:
            min = item*dict[item]
    print(sum(arr)-min)

for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    getResult(arr)
