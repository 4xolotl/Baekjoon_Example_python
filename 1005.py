t = int(input())
time = 0

for i in range(t):
    n, k = map(int, input().split())
    d = map(int, input().split())
    d = list(d)
    d1 = []
    for d2 in d:
        d3 = []
        d3.append(d2)
        d1.append(d3)
    d = d1
    time += d[0][0]
    for ii in range(k):
        x, y = map(int, input().split())
        d[x-1].append(y)
    w = int(input())
    for ii in range():
        time += max(d[ii])
    print(time)