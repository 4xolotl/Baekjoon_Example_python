def a(n, m):
    r = list(map(int, input().split()))
    mx=0
    for i in range(n-2):
        for ii in range(i+1, n-1):
            for iii in range(ii+1, n):
                s = r[i] + r[ii] + r[iii]
                if s>m:
                    continue
                elif s == m:
                    return s
                elif s<m and s>mx:
                    mx = s
    return mx

n, m = map(int, input().split())
print(a(n, m))