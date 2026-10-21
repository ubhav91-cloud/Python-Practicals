# Program 81: Check whether a year is a leap year

is_leap = lambda year: "Leap year" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "Not a leap year"
print(is_leap(2024))
