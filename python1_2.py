def check_error(n):
    if n.isdigit():
        n = int(n)
        if n < 2:
            return True
        else: return False
    else: return True

def palindrome_check(n):
    a = int(n)
    temp = 0
    start = 10**(a - 1)
    end = 10**a - 1
    for i in range(end, start - 1, -1):
        for j in range(i, start - 1, -1):
            x = i * j
            if x <= temp:
                break
            if str(x) == str(x)[::-1]:
                temp = x
    return temp

n = input()

if check_error(n): 
    print('Invalid')
    
else:
    largest_palindrome = palindrome_check(n)
    print(largest_palindrome)