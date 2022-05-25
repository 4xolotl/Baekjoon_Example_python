a = input()
a = (a)
c=0
s=0
if '-' in a:
    for i in range(len(a)):
        if a[i] == '-':
            p = a[:i].split('+')
            n = a[i+1:].replace('-', '/')
            n = n.replace('+', '/')
            n = n.split('/')
            break
    
    for i in p:
        p = map(int, p)
        c += sum(p)
    else:
        n = map(int, n)
        c -= sum(n)

    print(c)
    
else:
    p = a.split('+')
    p = map(int, p)
    print(sum(p))
