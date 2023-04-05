eu = int (input('Enter the electricity unit consumed:'))

if eu <= 50:
    amt = 50 * 0.50
    print('amount to be paid is:',amt)
elif eu >= 50 and eu <=150:
    amt = 50 * 0.50 + (eu-50) * 0.75
    print ('Amount to be paid is :',amt)
elif eu >= 150 and eu <=250:
    amt = 50 * 0.50 + 100*0.75 + (eu-150)*1.20
    print ('Amount to be paid is :',amt)
else:
    amt = 50 * 0.50 + 100*0.75 + 100*1.20 + (eu-250)*1.50
    print ('Amount to be paid is :',amt)
     
