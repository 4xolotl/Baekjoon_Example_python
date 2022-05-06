n, m = map(int, input().split())
ar1 = list(map(int, input().split()))

for i in range(max(ar1), 0, -1):
    s1=0
    for ii in range(n):
        s1 += ar1[ii]-i if (ar1[ii] > i) else 0
    if s1 >= m:
        print(i)
        break