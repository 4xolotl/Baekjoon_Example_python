n, k = map(int, input().split())
c=1

for i in range(n, n-k, -1):
    c*=i
for i in range(k, 1, -1):
    c//=i
print(c%10007)