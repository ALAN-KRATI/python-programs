a = input()
b = ""
for i in range(0,len(a)):
    if a[i].islower():
        b += a[i].upper()
    elif a[i].isupper():
        b += a[i].lower()
    else:
        b += a[i]

print(b)
