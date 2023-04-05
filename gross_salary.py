
bs = int (input('Enter the basic salary:'))

if bs <= 10000 :
    hra = bs * 0.2
    da = bs * 0.8

elif bs <= 20000:
    hra = bs * 0.25
    da = bs * 0.9

else:
    hra = bs * 0.3
    da = bs * 0.95


gs = bs + hra + da

print (gs)
    
    
