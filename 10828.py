n = int(input())
ar = []
for i in range(n):
    cm = input()
    if cm[:2] =='pu':
        num = int(cm.split()[-1])
        ar.append(num)
    elif cm[:2] =='po':
        if len(ar) == 0:
            print(-1)
        else:
            print(ar[-1])
            ar.pop(-1)
    elif cm[:2] =='si':
        print(len(ar))
    elif cm[:2] =='em':
        if len(ar) == 0:
            print(1)
        else:
            print(0)
    elif cm[:2] =='to':
        if len(ar) == 0:
            print(-1)
        else:
            print(ar[-1])