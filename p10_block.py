n = int(input('Enter the rows:'))
for i in range(1,n+1):
    if i == 1 or i == 5:
        print("*"*13)
    else:
        print("*" + " "*11 + "*")