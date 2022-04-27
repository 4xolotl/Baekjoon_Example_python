a, b= input().split()
a = int(a)
b = int(b)
d=0
for i in range(1, max(a, b)+1):
    if a%i==0 and b%i==0:
        c = i
print(c)
print(a*b//c)