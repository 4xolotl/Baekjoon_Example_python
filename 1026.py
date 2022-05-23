s=0
t = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(t):
    s += a[i] * b[i]
    
print(s)