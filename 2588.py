a = input()
b = input()
a, b = int(a), int(b)

print(a*(b%10))
print(a*((b//10)%10))
print(a*(b//100))
print(a*b)