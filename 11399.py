n = int(input())
ar = list(map(int, input().split()))

ar.sort()
s=0

for i in range(len(ar)):
    s += sum(ar[:i+1])

print(s)