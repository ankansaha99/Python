import calendar

leap_checker =calendar.isleap(2024)
print(leap_checker)
if(leap_checker == 1 ):
    print("Leap year")
else:
    print("Is not Leap year")

