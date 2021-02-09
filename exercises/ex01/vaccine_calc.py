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

CURRENT_POP: int = int(input("Population: "))
DOSES_ADMIN: int = int(input("doses administered: "))
DOSE_PER_DAY: int = int(input("doses per day: "))
TARGET_GOAL: int = int(input("target percent vaccinated:: "))

VACC_CURRENT_DATE: int = int(DOSES_ADMIN / 2)
POP_PERCENT_DECI: float = float(TARGET_GOAL / 100)
VACC_NEEDED: float = float(CURRENT_POP * POP_PERCENT_DECI)
REMAINDER_VACC: int = int(VACC_NEEDED - VACC_CURRENT_DATE)
DAYS_GOAL_REACHED: int = int((2 * REMAINDER_VACC) / DOSE_PER_DAY )

FUTURE: timedelta = timedelta(DAYS_GOAL_REACHED)
DAY_GOAL_MET: datetime = today + FUTURE
DATE: datetime = DAY_GOAL_MET.strftime("%B %d, %Y")

T_GOAL: str = str(TARGET_GOAL)
DAY: str = str(DAYS_GOAL_REACHED)
DATE_S: str = str(DATE)

print("We will reach " + T_GOAL + "% vaccination in " + DAY + " days, which falls on " + DATE_S + ".")