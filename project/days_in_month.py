import datetime

def days_in_month(year, month):
    x = datetime.date(year,month,1)
    if x.month <=11:
        difference = datetime.date(year,month+1,1) -x
        return difference.days
    elif x.month==12:
        difference_2 = datetime.date(year+1,1,1) -x
        return difference_2.days
print (days_in_month(1983,12))
