day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_of_year(day, month, year):
    day_of_years = 0
    if month > 12 or month < 1 or year <= 0 or (day not in day_in_month[month]):
        return 'Invalid'
    if is_leap(year):
        day_in_month[2] += 1
    else:
        if month == 2 and day == 29:
            return 'Invalid'
    
    for i in range(1, month):
        day_of_years += day_in_month[i]
    day_of_years += day
    
    if day_of_years > 366:
        return "Invalid"
    
    return day_of_years

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

day, month, year = map(int, input().split('-'))
result = day_of_year(day, month, year)

print(f"day of year: {result} is_leap: {is_leap(year)}")