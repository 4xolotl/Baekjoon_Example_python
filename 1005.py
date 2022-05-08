def requirement_list(r, x, y):
    r[y-1].append(x)
    return r

def get_list(r, w):
    if r[w]:
        process.append(get_list(r, r[i]))
    return process[w]

def techtree(r, x, y):
    tmp=0
    if r[len(r)//2]:
        r[x-1].append(x)
        r[x].append(y)
        print("kk")
    for i in range(len(r/2)):
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
    return r

def min_time(r):
    time=0
    for i in range(len(r)):
        if w in r[i]:
            index = i
            break
    for i in range(index):
        if r[ii]:
            time += cost[max(r[i])]
    return time+cost[w]

t = int(input())
time = 0
process = []

for i in range(t):
    r = []
    n, k = map(int, input().split())
    for ii in range(n*2-1):
        r.append([])
    D = list(map(int, input().split()))
    cost = dict(zip(list(range(1, n+1)), D))
    print(cost)
    for ii in range(k):
        a = list(map(int, input().split()))
        r = requirement_list(r, a[0], a[1])
    
        print(r)
    w = int(input())
    print(f"time: {min_time(w)}")
    
    
    