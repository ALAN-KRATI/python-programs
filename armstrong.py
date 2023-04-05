a = int(input('Enter the number to check:'))
sum = 0
temp = a
while temp > 0:
    digit = temp%10
    sum += digit**3
    temp //= 10

if a == sum:
    print('Armstrong')
else:
    print('Not armstrong') 
