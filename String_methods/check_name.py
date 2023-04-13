name=input("Enter your name:- ")
st="aeiouAEIOU"
v=c=0

for i in name:
    if i in st:
        v+=1
    else:
        c+=1    

print("vowel is ",v," consonent is ",c)        