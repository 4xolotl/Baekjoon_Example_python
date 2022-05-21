n = int(input())
a = list(input())

for i in range(n-1):
    tmp = list(input())
    for ii in range(len(a)):
        if a[ii] != '?':
            if a[ii] != tmp[ii]:
                a[ii] = '?'
for i in a:
    print(i, end='')