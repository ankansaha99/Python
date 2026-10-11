import calendar
day_checker=calendar.weekday(2022,10,31)
#print(day_checker)

print("Today is 👇↙️")
if (day_checker == 0):
    print("Monday")
elif (day_checker == 1):
    print("Tuesday")
elif (day_checker == 2):
    print("Wednesday")
elif (day_checker == 3):
    print("Thursday")
elif(day_checker == 4):
    print("Friday")
elif(day_checker == 5):
    print("Saturday")
elif (day_checker == 6):
    print("Sunday")
