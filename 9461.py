a = [1, 1, 1, 2, 2, 3]
b = []
t = int(input())
for j in range(t):
    b.append(int(input()))
    
for i in range(6, max(b)):
    a.append(a[i-5]+a[i-1])

for k in b:
    print(a[k-1])