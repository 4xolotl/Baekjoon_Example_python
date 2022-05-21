t = int(input())

for i in range(t):
    c=1
    a, b = map(int, input().split())
    for ii in range(b-a+1, b+1):
        c *= ii
    for ii in range(1, a+1):
        c = c // ii
    
    print(c)