n = int(input('Enter the rows:'))
c = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+c), end =' ')
        c+=1
    print()