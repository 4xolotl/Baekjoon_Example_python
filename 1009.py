t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    for ii in range(b):
        a*=a
        a%=10
    print(a)