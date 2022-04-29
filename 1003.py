a = [1, 0]
l = []

n = int(input())

for i in range(n):
    j = int(input())
    l.append(j)
    
for i in range(2, max(l)+2):
    a.append(a[i-2] + a[i-1])

for i in l:
    print(f"{a[i]} {a[i+1]}")