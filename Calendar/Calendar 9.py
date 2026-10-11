import calendar

lc=int(input("Enter year to check leap year : "))

leap_checker =calendar.isleap(lc)
print(leap_checker)
if(leap_checker == 1 ):
    print(lc,"is Leap year ✅")
else:
    print(lc,"is not Leap year ❌")

print("Edit Done")

