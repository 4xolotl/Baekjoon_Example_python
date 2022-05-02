t = int(input())
time = 0

def tectree(r, x, y):
    tmp=0
    if x in r:
        for i in range(len(r)):
            for ii in range(len(r[i])):
                if x == ii:
                    r[i+1].append(y)
                    tmp = 1
                    break
            if tmp == 1:
                break
    elif y in r[:]:
        for i in range(len(r)):
            for ii in range(len(r[i])):
                if y == ii:
                    r[i].append(x)
                    tmp = 1
                    break
            if tmp == 1:
                break
    else:
        r[x-1].append(x)
        r[x].append(y)
    return r
    

for i in range(t):
    r = []
    n, k = map(int, input().split())
    for ii in range(n):
        r.append([])
    D = list(map(int, input().split()))
    tech = dict(zip(list(range(1, n+1)), D))
    print(tech)
    for ii in range(k):
        a = list(map(int, input().split()))
        r = tectree(r, a[0], a[1])
        print(r)