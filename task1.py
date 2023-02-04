day = int(input("Enter day: "))
year = day // 365
week = (day - year * 365) // 7
day = day - year * 365 - week * 7
print(f'Years:{year}\nWeeks: {week}\nDays:{day}\n')


