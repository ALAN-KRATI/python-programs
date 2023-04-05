
a = int (input('Enter your amount for withdrawal:'))

amt = ( a - 100)

twok = amt//2000
amt %= 2000

fiveh = amt//500
amt %= 500

twoh = amt//200
amt %= 200

oneh = amt//100 + 1
amt %= 100

print('Number of 2000 notes: %d'%twok)
print('Number of 500 notes: %d'%fiveh)
print('Number of 200 notes: %d'%twoh)
print('Number of 100 notes: %d'%oneh)

