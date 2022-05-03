t = int(input())
time = 0

def techtree(r, x, y):
    for i in range(len(r/2)):
        tmp=0
        if x in r[i]:
            if y not in r[i+1]:
                r[i+1].append(y)
                print("x")
            tmp=1
            break
    if tmp == 0:
        for i in range(len(r/2)):
            if y in r[i]:
                if x not in r[i]:
                    r[i].append(x)
                    print("y")
                tmp=1
                break
    if tmp == 0:
        r[x-1].append(x)
        r[x].append(y)
        print("kk")
    return r


for i in range(t):
    r = []
    n, k = map(int, input().split())
    for ii in range(n*2):
        r.append([])
    D = list(map(int, input().split()))
    cost = dict(zip(list(range(1, n+1)), D))
    print(cost)
    for ii in range(k):
        a = list(map(int, input().split()))
        r = techtree(r, a[0], a[1])
        print(r)
    w = int(input())
    for ii in range(len(r)):
        if w in r[ii]:
            index = ii
            break
    for ii in range(index):
        if r[ii]:
            time += cost[max(r[ii])]
    print(f"time: {time+cost[w]}")