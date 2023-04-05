n = int(input('Enter the rows:'))
c = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c , end = " ")
        if (c<9):
            c += 1
        else:
            c = 1
    print()      
