r = int(input('Enter the numbers of rows:'))
for i in range(1,r+1):
   print("*"*i + " "*((2*r-2*i)+1) + "*"*i)
print("*"*(2*r+1))
    