name=input("Enter ur name\n")
ur_interest=input("Enter ur interest\n")

print("Format() method is making format of given paragraph or sentence. we can use with 2 ways as example given below follow this example")

s1w=f"My name is {name}, and my interest is {ur_interest}."
s2w="My name is {}, and my interest is {}.".format(name,ur_interest)

print("way first:-\n",s1w)
print("way second:-\n",s2w)

