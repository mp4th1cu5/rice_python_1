def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value*(1+rate_per_period)**periods
    # Put your code here.

#print(future_value(500,0.04,10,10))
print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))
