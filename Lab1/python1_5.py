def sort_number():
    my_list.sort()
    
def check_error():
    for num in my_list:
        if not num.isdigit() or int(num) < 0 or int(num) > 9 or len(my_list) == 1:
            return False
    return True


my_list = input().split()


    
if len(my_list) > 10:
    print("Invalid")
    
elif check_error():
    sort_number()
    if my_list[0] == '0':
        for i in range(1, len(my_list)):
            if my_list[i] != '0':
                my_list[0], my_list[i] = my_list[i], my_list[0]
                break

    for i in my_list:
        print(i, end='')
        
else:
    print("Invalid")
