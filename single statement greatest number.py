a = int (input('Enter the first number:'))
b = int (input('Enter the second number:'))
c = int (input('Enter the third number:'))

out = a if a >= b and a >=c else b if b >= a and b >=c else c

print (out)
