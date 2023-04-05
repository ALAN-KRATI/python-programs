lund = list(map(int,input().split(' ')))

x = int(input("Enter the number to remove  : "))

y = lund.count(x)

for i in range(y):
    lund.remove(x)

print(lund)

