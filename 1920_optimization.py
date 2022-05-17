n = int(input())
An = set(map(int, input().split()))
m = int(input())
Mn = list(map(int, input().split()))

for i in range(m):
    if Mn[i] in An:
        print(1)
    else:
        print(0)