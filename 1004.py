t = int(input())

for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    k=0
    for ii in range(n):
        cx, cy, cr = map(int, input().split())
        f = (cx-x1)**2 + (cy-y1)**2 < cr**2
        s = (cx-x2)**2 + (cy-y2)**2 < cr**2
        if f != s:
            k += 1
    print(k)