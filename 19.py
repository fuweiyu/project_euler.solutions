def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31

# Starting from 1 Jan 1900 (Monday)
current_day_of_week = 0  # 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
sunday_count = 0

# Move to 1 Jan 1901
for year in range(1900, 1901):
    for month in range(1, 13):
        current_day_of_week = (current_day_of_week + days_in_month(year, month)) % 7

# Count Sundays on the first of the month from 1 Jan 1901 to 31 Dec 2000
for year in range(1901, 2001):
    for month in range(1, 13):
        if current_day_of_week == 6:  # 6 = Sunday
            sunday_count += 1
        current_day_of_week = (current_day_of_week + days_in_month(year, month)) % 7

print("Number of Sundays that fell on the first of the month:", sunday_count)
