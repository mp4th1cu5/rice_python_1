import datetime

def is_valid(year,month,day):
    if year in range (datetime.MINYEAR,datetime.MAXYEAR) and month in range (1,13) and day <= days_in_month(year,month):
        return True
    else:
        return False
print (is_valid(1983,2,29))
