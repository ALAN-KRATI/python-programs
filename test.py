enemy, friend = 5,2
st = "No better friend no worse enemy".split()
re = st[enemy%20] and None if enemy + friend < len(st) else st[friend%20] 
print(re,eval(re))