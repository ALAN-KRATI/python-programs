'''c = [] #empty list
a = [1,2,3,4,4]

s = "abcd"

d = list(s)

print(c+a+d)
'''

#CREATING LIST FROM USER INPUT -1
'''x = int(input("Enter the size for the list : "))
l = []
for i in range(x) :
    l.append(input())

print(l)
'''

#CREATING LIST FROM USER INPUT -2
'''
x = list(map(int,input().split(' ')))
print(x)
'''

s = "Hello world jai shree ram"

'''
l = s.split(' ')
l.reverse()

for i in l :
    print(i,end=' ')

'''
'''
x = eval(input())

print(x,type(x))
'''
#remove items in a list

l = [1,2,3,4,5]

#l.remove(2)
#l.pop(3)

del l[1]




print(l)