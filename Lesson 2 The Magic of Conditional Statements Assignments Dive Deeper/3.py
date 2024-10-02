# 3. Leap Year Explorer
leapyearcheck = int(input("Welcome to Leap Year Checker. Please enter a year: "))
if (leapyearcheck % 4 == 0 and leapyearcheck % 100 != 0) or (leapyearcheck % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")
