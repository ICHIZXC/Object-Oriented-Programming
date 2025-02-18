def check_error():
    if a < 0 or a > 9:
        return True
    
a = int(input())

if check_error():
    print('Invalid')
    
else:
    print(a + (11*a) + (111*a) + (1111*a))
