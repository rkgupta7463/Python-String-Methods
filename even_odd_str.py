name=input("Enter name :- ")

##by lenght function 
print("\nBy lenght function\n")
for i in range(len(name)):
    if i%2==0:
        print("Even place :- ",name[i])
    else:    
        print("Odd place :- ",name[i])    

##by index funtion
print("\nBy index function\n")
for i in name:
    if name.index(i)%2==0:
        print("Even :- ",i)
    else:
        print("Odd :- ",i)    
              
#combine string at even place & odd place
print("\nCombined string \n")
o=""
e=""
for i in range(len(name)):
    if i%2==0:
        e=e+name[i]
    else:
        o=o+name[i]
print("Even:- ",e)        
print("Odd:- ",o)        