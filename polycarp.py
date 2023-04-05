s = list(map(str,input().split(' ')))

s = ''.join(s)

k = ' '
c = 0
max = 0
for i in s:
    
    if k not in s:
        c = s.count(i)
        k += i
    
    if max < c:
        max = c

print(max)
