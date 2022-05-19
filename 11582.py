n = int(input())
a = list(map(int, input().split()))
k = int(input())
b = []

for i in range(0, n, n//k):
    b.append(sorted(a[i:i+n//k]))
for i in range(len(b)):
    for ii in b[i]:
        print(ii, end=' ')
