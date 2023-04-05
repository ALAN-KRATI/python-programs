r = int(input('Enter the rows:'))
for i in range(1,r+1):
    print(" "*(r-i) + "*"*(2*i-1) )
for i in range(2,r+1):
    print(" "*(i-1)  + "*"*(2*((r+1)-i)-1))