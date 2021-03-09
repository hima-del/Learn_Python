# to check wheather a given year is leap year or not
year = int(input("enter the year : "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("given year is leap year")
        else:
            print("given year is not leap year")
    else:
        print("given year is leap year")
else:
    print("given year is not leap year")                     