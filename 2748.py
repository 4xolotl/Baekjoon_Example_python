a= [0, 1]
k = int(input())
for i in range(2, k+1):
    a.append(a[i-2]+a[i-1])
print(a[k])