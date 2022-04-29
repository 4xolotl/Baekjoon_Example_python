a = []
s = 0

a[:4] = input().split()

for i in range(5):
    n = int(a[i])
    s += n*n
    
print(s%10)