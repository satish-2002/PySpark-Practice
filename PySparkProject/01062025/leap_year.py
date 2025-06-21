###Python program to check weather given year is leap year or not
year = int(input("Enter year in yyyy format:"))

# year divisible by 100(century year) and also divisible by 400 is a leap year
if (year % 100 == 0) and (year % 400 == 0):
    print("{0} is a leap year".format(year))
# year not divisible by 100(century year) and divisible by 4 is a leap year
elif (year % 100 != 0) and (year % 4 == 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))