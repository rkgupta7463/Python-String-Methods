name=input("Enter ur paragraph\n").split()

m=""
for i in name:
    if len(i)>len(m):
        m=i
print(m)