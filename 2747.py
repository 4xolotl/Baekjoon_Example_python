a = [0] * 46
a[:3] = [0, 1, 1]

for i in range(3, 46):
    a[i] = a[i-2] + a[i-1]
    
i = int(input())
print(a[i])