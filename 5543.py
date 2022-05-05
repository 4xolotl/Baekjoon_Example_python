a=[]
for i in range(5):
    a.append(int(input()))
print(f"{min(a[0:3])+min(a[3:5])-50}")