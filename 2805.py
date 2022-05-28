n, m = map(int, input().split())
ar1 = list(map(int, input().split()))

def target(ar, n):
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

target(ar1, m)