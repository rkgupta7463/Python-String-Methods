text1=" 123456 78910      "

print("This strip method is avoid the extra space from last.")
print("Lenght of text is ",len(text1),"without strip method.")
t=text1.strip()
print("Lenght of text is ",len(t),"with strip method.")
print(t)

text2="  123456 78910      "

print("This strip method is avoid the extra space from right side.")
print("Lenght of text is ",len(text2),"without strip method.")
text2.rstrip()
print("Lenght of text is ",len(t),"with strip method.")
print(t)


text3="  123456 78910      "

print("This strip method is avoid the extra space from left side.")
print("Lenght of text is ",len(text2),"without strip method.")
text3.lstrip()
print("Lenght of text is ",len(t),"with strip method.")
print(t)