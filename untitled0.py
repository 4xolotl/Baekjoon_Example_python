
while (True):
    m = int(input("1: 본문\n2: 어휘"))
    if m==1:
        a = input("입력: ")
        print("====================")
        
        for i in range(0, len(a)):
            if a[i-1]=="." and a[i]==" ":
                print()
            else:
                print(a[i], end='')
                
        
    elif m==2:
        a = input("입력: ")

        print("====================")

        for i in a:
            if i != "\n":
                if i == '	':
                    print(' ', end='')
                else:
                    print(i, end='')
    elif m==3:
        break
    