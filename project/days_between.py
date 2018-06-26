import datetime
def days_in_month(year, month):
    x = datetime.date(year,month,1)
    if x.month <=11:
        difference = datetime.date(year,month+1,1) -x
        return difference.days
    elif x.month==12:
        difference_2 = datetime.date(year+1,1,1) -x
        return difference_2.days

def is_valid(year,month,day):
    if year in range (datetime.MINYEAR,datetime.MAXYEAR) and month in range (1,13) and day <= days_in_month(year,month):
        return True
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    if is_valid (year1,month1,day1) and is_valid (year2,month2,day2) == True and datetime.date(year2,month2,day2)>datetime.date(year1,month1,day1):
        days_betw = datetime.date(year2,month2,day2) - datetime.date(year1,month1,day1)
        return days_betw.days
    else:
        return 0
print (days_between(2000,11,19,2018,6,25))
