
def leap_year(year):
    """ Take year as input and check weither
    it is leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False 
        else:
            return True
    else:
        return False 

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year) and month == 2:
        return 29
    return month_days[month -1]    



year = int(input("Enter year "))
month = int(input("Enter month "))
days = days_in_month(year, month)
print(days)
