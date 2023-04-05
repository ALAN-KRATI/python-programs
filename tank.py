t = int(input('Enter the time:'))
v = 785
tf = 15*t
if v<tf:
    print("Tank is overfilled")
elif v == tf:
    print('Tank is full')
else:
    print('Tank is underfilled')
    df = v-tf
    h = df/78.5
    print(f'Remaining height to be filled is {h}')