n = int(input())
a = list(map(int, input().split()))
k = int(input())

for i in range(0, n-k+1, 2**k):
    print(sorted(a[i:i+k]), end='')