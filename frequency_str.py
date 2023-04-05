s = input('Enter a String:')
ls = { }
for i in s:
    if i in ls:
        ls[i] += 1
    else:
        ls[i] = 1

print('The frequency of characters in the given string is:\n' + str(ls))

