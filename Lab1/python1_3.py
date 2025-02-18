import math

def calculate_parking_fee(a, b, c, d):
    time1 = a * 60 + b
    time2 = c * 60 + d
    duration = time2 - time1
    hours = math.ceil(duration / 60)

    if b >= 60 or d >= 60 or 0 < a < 7 or 0 < c < 7 or a > 23 or c > 23 or time2 <= time1 or a < 0 or b < 0 or c < 0 or d < 0:
        return "Invalid"
    
    
    elif duration <= 15:
        return 0
    elif duration > 15 and hours <= 3:
        return 10 * hours
    elif 4 <= hours < 6:
        return 30 + (20 * (hours - 3))
    else:
        return 200 * math.ceil(hours / 24)

a, b, c, d = map(int, input().split())
fee = calculate_parking_fee(a, b, c, d)
print(fee)  
