def remove_dupes_sort(x):
    return sorted(list(dict.fromkeys(x)))

my_list = input()[1:-1]

if any(c.isalpha() for c in my_list):
    print("Invalid")
else:
    my_list = remove_dupes_sort(map(int, my_list.split(',')))
    if len(my_list) == 1: print('Invalid')
    else: print(max(my_list[0] * my_list[1], my_list[-2] * my_list[-1]))
