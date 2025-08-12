class LeapYear:
    def __init__(self, year):
        self.year = year
    
    def is_leap_year(self):
        if self.year % 400 == 0:
            return True
        elif self.year % 4 == 0 and self.year % 100 != 0:
            return True
        else:
            return False

year = int(input("Enter the year to check if it's a Leap Year: "))
obj = LeapYear(year)

if obj.is_leap_year():
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
