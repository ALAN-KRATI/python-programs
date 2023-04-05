a = input('Enter your own character:')

if (( a >= 'a' and a <= 'z') or ( a >= 'A' and a <= 'Z')):
    print('The given character is an Alphabet')
    
elif ( a >= '0' and a <= '9'):
    print('The given character is a Digit')
    
else:
    print('The given character is a special character')
