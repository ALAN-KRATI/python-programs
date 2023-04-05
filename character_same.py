a = input('Enter your string:')
b = a.casefold()
flag = 0
for i in range(0,len(a)):
    if b[0]!=b[i]:
      flag = 1
    
if flag == 0:
    print('All the characters are same.')
else:
    print('None')