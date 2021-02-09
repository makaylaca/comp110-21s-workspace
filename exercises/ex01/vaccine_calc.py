"""A vaccination calculator."""

__author__ = "730342554"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

today: datetime = datetime.today()

current_pop: int = int(input("Population: "))
doses_admin: int = int(input("doses administered: "))
dose_per_day: int = int(input("doses per day: "))
target_goal: int = int(input("target percent vaccinated:: "))

vacc_current_date: int = int(doses_admin / 2)
pop_percent_deci: float = float(target_goal / 100)
vacc_needed: float = float(current_pop * pop_percent_deci)
remainder_vacc: int = int(vacc_needed-vacc_current_date)
days_goal_reached: int = int((2*remainder_vacc)/dose_per_day )

future: timedelta = timedelta(days_goal_reached)
day_goal_met: datetime = today + future
date: datetime = day_goal_met.strftime("%B %d, %Y")

t_goal: str = str(target_goal)
day: str = str(days_goal_reached)
date_s: str = str(date)

print("We will reach " + t_goal + "% vaccination in " + day + " days, which falls on " + date_s + ".")