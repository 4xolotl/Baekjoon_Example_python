n = int(input())
ar1 = set(map(int, input().split()))
m = int(input())
ar2 = list(map(int, input().split()))

for i in ar2:
    if i in ar1:
        print("1", end=' ')
    else:
        print("0", end=' ')