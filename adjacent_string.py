s = input("Enter the string :")

k = ' '
c = 0
max = 0
for i in s:
    
    if k not in s:
        c = s.count(i)
        k += i
    
    if max < c:
        max = c

count = len(s) - max
if(max<= count):
    print("TRUE")
else:
    print("FALSE")
