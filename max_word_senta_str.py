name=input("Enter your paragraph\n").split()

m=""
for i in name:
    if len(i)>len(m):
        m=i
print("This word is maximum lenght :- ",m)