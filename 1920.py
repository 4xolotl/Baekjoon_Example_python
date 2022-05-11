n = int(input())
An = list(map(int, input().split()))
An.sort()
m = int(input())
Mn = list(map(int, input().split()))

def target(t, ar, n):
    st, en = 0, n
    while st <= en:
        mid = (st + en) // 2
        if ar[mid] == t:
            return 1
        elif ar[mid] > t:
            en = mid - 1
        else:
            st = mid + 1
    return 0
        
    
for i in Mn:
    print(target(i, An, n-1))