day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day, month, year):
    if is_leap(year):
        day_in_month[2] = 29
    else:
        day_in_month[2] = 28

    if month < 1 or month > 12 or day < 1 or day > day_in_month[month]:
        return -1

    return sum(day_in_month[:month]) + day

def total_day_in_year(year):
    return 366 if is_leap(year) else 365

def date_diff(date1, date2):
    day1, month1, year1 = map(int, date1.split('-'))
    day2, month2, year2 = map(int, date2.split('-'))

    total1 = day_of_year(day1, month1, year1)
    total2 = day_of_year(day2, month2, year2)

    if total1 == -1 or total2 == -1:
        return 'Invalid'

    if year1 == year2:
        return abs(total1 - total2) + 1

    elif year2 - year1 == 1:
        return (total_day_in_year(year1) - total1) + total2 + 1

    else:
        total_day = 0
        for i in range(year1 + 1, year2):
            total_day += total_day_in_year(i)

        return total_day + total2 + (total_day_in_year(year1) - total1) + 1

date = input()
date1, date2 = date.split(',')

answer = date_diff(date1, date2)
print(answer)
