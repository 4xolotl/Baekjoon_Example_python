a = int(input())
for i in range(a):
    st=input()
    c=0
    t=0
    for ii in st:
        if ii=='(':
            c += 1
        elif ii ==')':
            c -= 1
        if c<0:
            print("NO")
            t=1
            break
    if c==0 and t==0:
        print("YES")
    elif c != 0 and t==0:
        print("NO")